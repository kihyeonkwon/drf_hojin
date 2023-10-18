from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView

from articles.models import Article, Comment
from articles.serializers import ArticleSerializer, CommentSerializer

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        

class ArticleDetailView(APIView):
    def get(self, request, article_id):
        article = Article.objects.get(pk=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    

class CommentView(APIView):
    def post(self, request, article_id):
        serializer = CommentSerializer(data=request.data)   
        if serializer.is_valid():
            serializer.save(article_id=article_id, user=request.user) 
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def get(self, request, article_id):
        comments = Comment.objects.filter(article_id=article_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)