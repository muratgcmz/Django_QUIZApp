from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
    @property
    def quiz_count(self):
        return self.quiz_set.count()

class Quiz(models.Model):
    title = models.CharField(max_length=100, verbose_name="Quiz Title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
                verbose_name_plural = "Quizzes"
    @property
    def question_count(self):
        return self.question_set.count()


class Updated(models.Model):
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True




class Question(Updated):

    SCALE = (
        (0, "Beginner"),
        (1, "Intermediate"),
        (2, "Advanced"),
    )

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, verbose_name="question")
    difficulty = models.IntegerField(choices=SCALE)
    date_created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class Answer(Updated):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answer")
    answer_text = models.CharField(max_length=250)
    is_right = models.BooleanField(default=False)
   

    def __str__(self):
        return self.answer_text
