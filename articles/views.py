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
    
    def post(self, request):
        print('post요청')
        print(request.data)
        print(request.user)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        

class ArticleDetailView(APIView):
    def get(self, request, article_pk):
        article = Article.objects.get(pk=article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)