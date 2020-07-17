from django.urls import path, include
from news import views
# from news.views import NewsList, NewsDetail, SearchView, NewsYearArchiveView, NewsMonthArchiveView, NewsDayArchiveView

urlpatterns = [
    path('search/', views.SearchView.as_view(), name='search'),
    path('', views.NewsArchiveView.as_view(), name='news'),
    path('detail/<slug:slug>', views.NewsDetail.as_view(), name='news-detail'),
    path('<int:year>/', views.NewsYearArchiveView.as_view(), name='year'),
    path('<int:year>/<int:month>/',
         views.NewsMonthArchiveView.as_view(month_format='%m'), name='month'),

    path('<int:year>/<int:month>/<int:day>/',
         views.NewsDayArchiveView.as_view(month_format='%m'), name='days'),


]
