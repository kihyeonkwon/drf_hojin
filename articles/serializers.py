from rest_framework import serializers
import users
from users.models import MyUser

from users.serializers import UserSerializer

from .models import Article, Comment

class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 'name', 'id']



class CommentSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    # user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'updated_at', 'user']


    # def get_user(self, obj):
    #     return obj.user.email
    




class ArticleSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'image','comments', 'user' ]





