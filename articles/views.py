from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView

from articles.models import Article
from articles.serializers import ArticleSerializer

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)    