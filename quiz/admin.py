from django.contrib import admin
from .models import Category, Quiz, Question, Answer
import nested_admin


class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 5
    max_num = 8

class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline]
    extra = 1
    max_num = 10

class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionInline]


admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)




