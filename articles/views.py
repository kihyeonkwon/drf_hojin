from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
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
    
    def put(self, request, article_id):
        article = Article.objects.get(pk=article_id)

        if article.user != request.user:
            return Response(status=403)

        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)



    

    def delete(self, request, article_id):
        if not request.user.is_authenticated:
            return Response(status=401)
        article = Article.objects.get(pk=article_id)
        if article.user != request.user:
            return Response(status=403)
        else:
            article.delete()
            return Response(status=204)
    

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

    
class CommentDetailView(APIView):
    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        if comment.user != request.user:
            return Response(status=403)
        
        comment.delete()
        return Response(status=204)