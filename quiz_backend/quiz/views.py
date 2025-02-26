from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from .models import User, Quiz, Question, QuestionOption, QuizAttempt, UserResponse
from .serializers import UserSerializer, QuizSerializer, QuestionSerializer, QuestionOptionSerializer, QuizAttemptSerializer, UserResponseSerializer

# Rate limiting: 100 requests per second per user
RATE_LIMIT = '100/s'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionOptionViewSet(viewsets.ModelViewSet):
    queryset = QuestionOption.objects.all()
    serializer_class = QuestionOptionSerializer

class QuizAttemptViewSet(viewsets.ModelViewSet):
    queryset = QuizAttempt.objects.all()
    serializer_class = QuizAttemptSerializer

    @method_decorator(ratelimit(key='user', rate=RATE_LIMIT))
    def create(self, request, *args, **kwargs):
        user = request.user
        quiz_id = request.data.get('quiz')
        responses = request.data.get('responses', [])

        # Calculate the score
        score = 0
        for response in responses:
            question_id = response.get('question')
            selected_option_id = response.get('selected_option')

            # Check if the selected option is correct
            selected_option = QuestionOption.objects.get(id=selected_option_id)
            if selected_option.is_correct:
                score += selected_option.question.marks

        # Create the quiz attempt
        quiz_attempt = QuizAttempt.objects.create(
            user=user,
            quiz_id=quiz_id,
            score=score,
            completed=True
        )

        # Create user responses
        for response in responses:
            UserResponse.objects.create(
                attempt=quiz_attempt,
                question_id=response.get('question'),
                selected_option_id=response.get('selected_option')
            )

        return Response({'score': score}, status=status.HTTP_201_CREATED)

class UserResponseViewSet(viewsets.ModelViewSet):
    queryset = UserResponse.objects.all()
    serializer_class = UserResponseSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuizResultsView(APIView):
    @method_decorator(ratelimit(key='user', rate=RATE_LIMIT))
    def get(self, request, quiz_id, user_id):
        try:
            # Fetch the quiz attempt for the user
            quiz_attempt = QuizAttempt.objects.get(quiz_id=quiz_id, user_id=user_id)
            user_responses = UserResponse.objects.filter(attempt=quiz_attempt)

            # Prepare the response data
            results = {
                'quiz_title': quiz_attempt.quiz.title,
                'user_score': quiz_attempt.score,
                'total_score': quiz_attempt.quiz.total_score,
                'responses': []
            }

            for response in user_responses:
                results['responses'].append({
                    'question': response.question.question_text,
                    'selected_option': response.selected_option.option_text,
                    'correct_option': response.question.options.get(is_correct=True).option_text,
                    'is_correct': response.selected_option.is_correct
                })

            return Response(results, status=status.HTTP_200_OK)
        except QuizAttempt.DoesNotExist:
            return Response({'error': 'Quiz attempt not found'}, status=status.HTTP_404_NOT_FOUND)