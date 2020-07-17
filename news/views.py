from django.shortcuts import render
from django.http import HttpResponse
from .models import News
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView, MonthArchiveView, WeekArchiveView, DayArchiveView, ArchiveIndexView
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone


class NewsArchiveView(ArchiveIndexView):
    date_field = "create_at"
    model = News
    paginate_by = 2
    template_name = 'news.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        queryset = super(NewsArchiveView, self).get_queryset()
        current = datetime.today() - timedelta(days=int(60))
        return queryset.filter(create_at__gte=current).order_by('-create_at')


class NewsDetail(DetailView):
    model = News
    template_name = 'news_detail.html'


class NewsYearArchiveView(YearArchiveView):
    queryset = News.objects.all()
    paginate_by = 2
    date_field = "create_at"
    make_object_list = True
    allow_empty = True


class NewsMonthArchiveView(MonthArchiveView):
    queryset = News.objects.all()
    date_field = "create_at"
    paginate_by = 2
    allow_empty = True


class NewsDayArchiveView(DayArchiveView):
    queryset = News.objects.all()
    date_field = "create_at"
    paginate_by = 2
    allow_empty = True


class SearchView(ListView):
    model = News
    template_name = 'news.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(
            Q(title__icontains=query) | Q(subtitle__icontains=query)
        )

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
