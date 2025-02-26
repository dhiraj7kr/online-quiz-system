from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

 # Add related_name to avoid clashes with auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='quiz_users',  # Unique related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='quiz_users',  # Unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    no_of_questions = models.IntegerField()
    total_score = models.IntegerField()
    duration = models.IntegerField()  # Duration in minutes

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    marks = models.IntegerField()
    duration = models.IntegerField(default=60)  # Time duration for the question in seconds

class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.TextField()
    is_correct = models.BooleanField(default=False)

class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

class UserResponse(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(QuestionOption, on_delete=models.CASCADE)