from rest_framework import serializers
from .models import User, Quiz, Question, QuestionOption, QuizAttempt, UserResponse

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_admin']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'no_of_questions', 'total_score', 'duration']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'question_text', 'marks', 'duration']

class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ['id', 'question', 'option_text', 'is_correct']

class QuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = ['id', 'user', 'quiz', 'score', 'completed']

class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = ['id', 'attempt', 'question', 'selected_option']