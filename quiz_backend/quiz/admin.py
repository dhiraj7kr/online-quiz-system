from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Quiz, Question, QuestionOption, QuizAttempt, UserResponse

# Register the custom User model
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_admin', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

# Register Quiz model
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'no_of_questions', 'total_score', 'duration')
    search_fields = ('title',)

# Register Question model
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'question_text', 'marks')
    list_filter = ('quiz',)
    search_fields = ('question_text',)

# Register QuestionOption model
@admin.register(QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    list_display = ('question', 'option_text', 'is_correct')
    list_filter = ('question',)
    search_fields = ('option_text',)

# Register QuizAttempt model
@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'completed')
    list_filter = ('quiz', 'completed')
    search_fields = ('user__username', 'quiz__title')

# Register UserResponse model
@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('attempt', 'question', 'selected_option')
    list_filter = ('attempt', 'question')
    search_fields = ('attempt__user__username', 'question__question_text')