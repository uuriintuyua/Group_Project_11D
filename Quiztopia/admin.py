from django.contrib import admin
from Quiztopia.models import User, Quiz, Question, Answer

class UserAdmin(admin.ModelAdmin):

    list_display = ('username', 'points', 'quizzes_taken', 'quizzes_created')

class QuizAdmin(admin.ModelAdmin):

    list_display = ('quiz_ID', 'quiz_title', 'category', 'difficulty','upvotes','creator')

class QuestionAdmin(admin.ModelAdmin):

    list_display = ('question_ID','question_text','quiz_ID')

class AnswerAdmin(admin.ModelAdmin):

    list_display = ('answer_ID','answer_text','is_correct','question_ID')

admin.site.register(User, UserAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

