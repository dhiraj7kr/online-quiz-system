from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, QuizViewSet, QuestionViewSet, QuestionOptionViewSet, QuizAttemptViewSet, UserResponseViewSet, RegisterView, QuizResultsView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'options', QuestionOptionViewSet)
router.register(r'attempts', QuizAttemptViewSet)
router.register(r'responses', UserResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('quizzes/<int:quiz_id>/results/<int:user_id>/', QuizResultsView.as_view(), name='quiz-results'),
]