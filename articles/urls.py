from django.urls import path
# from . import views
from .views import ArticleView, ArticleDetailView

urlpatterns = [
    path('', ArticleView.as_view()),
    path("<int:article_pk>/", ArticleDetailView.as_view()),
]
