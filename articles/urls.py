from django.urls import path
# from . import views
from .views import ArticleView, ArticleDetailView, CommentView

urlpatterns = [
    path('', ArticleView.as_view()),
    path("<int:article_id>/", ArticleDetailView.as_view()),
    path("<int:article_id>/comment/", CommentView.as_view()),
]
