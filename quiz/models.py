from django.db import models
import uuid


class QuizCategory(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "QuizCategories"

    def __str__(self):
        return self.category_name


class Quiz(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, max_length=8, default=uuid.uuid4)
    quiz_name = models.CharField(max_length=200)
    category = models.ForeignKey(
        QuizCategory, related_name='quiz_category', on_delete=models.CASCADE)
    no_of_question = models.PositiveIntegerField(default=0)
    publish_date = models.DateTimeField()
    is_published = models.BooleanField()
    quiz_duration = models.DurationField(default='00:00:00')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quiz_name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_question', blank=True, null=True)
    question_text = models.CharField(max_length=1000)
    mark = models.PositiveIntegerField(default=1)
    option_A = models.CharField(max_length=200)
    option_B = models.CharField(max_length=200)
    option_C = models.CharField(max_length=200)
    option_D = models.CharField(max_length=200)
    choose = (
        ('A', 'option_A'),
        ('B', 'option_B'),
        ('C', 'option_C'),
        ('D', 'option_D')
    )
    answer = models.CharField(max_length=1, choices=choose)

    def __str__(self):
        return self.question_text
