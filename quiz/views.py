from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.utils import timezone
from quiz.models import Quiz, Question


class TestView(TemplateView):
    template_name = 'quiz_home.html'


class DemoQuiz(ListView):
    template_name = 'demo_test.html'
    model = Quiz
    context_object_name = 'test'

    def get_queryset(self):
        queryset = super(DemoQuiz, self).get_queryset()
        queryset = queryset.filter(category__category_name='Demo')
        return queryset

    def get_context_data(self, **kwargs):
        """
        {
            que id: ['who the president of india?', 'Dr. Pranav Mukhargee', 'Ramanath Kovind', 'Narendra Modi', 'Amit shah'], 
            que id: ['who the president of india?', 'Dr. Pranav Mukhargee', 'Ramanath Kovind', 'Narendra Modi', 'Amit shah'], 
            que id: ['who the president of india?', 'Dr. Pranav Mukhargee', 'Ramanath Kovind', 'Narendra Modi', 'Amit shah'], 
            que id: ['who the president of india?', 'Dr. Pranav Mukhargee', 'Ramanath Kovind', 'Narendra Modi', 'Amit shah'], 
        }
        """
        context = super(DemoQuiz, self).get_context_data(**kwargs)
        context['quiz_question'] = Question.objects.filter(quiz__id=context['object_list'][0].id)
        return context


# calculate