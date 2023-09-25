from django.urls import path
# from . import views
from .views import ArticleView

urlpatterns = [
    path('', ArticleView.as_view())
]
