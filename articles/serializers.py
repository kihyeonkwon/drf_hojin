from rest_framework import serializers
import users
from users.models import MyUser

from users.serializers import UserSerializer

from .models import Article

class ArticleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['email', 'name']


class ArticleSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'image', ]





