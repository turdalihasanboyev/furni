from django.urls import path

from .views import ArticlePageView


urlpatterns = [
    path('article/', ArticlePageView.as_view(), name='article'),
]
