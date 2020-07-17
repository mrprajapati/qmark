from django.contrib import admin
# from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline
from quiz.models import QuizCategory, Quiz, Question


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0


class QuizAdmin(admin.ModelAdmin):
    search_fields = ['publish_date', 'quiz_name']
    list_filter = ('publish_date', 'category__category_name', )
    list_display = ('quiz_name', 'publish_date', 'category', 'create_at')
    inlines = [QuestionInline]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizCategory)
