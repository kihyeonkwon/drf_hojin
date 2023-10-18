from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 생성될 때 자동으로 넣어줌
    updated_at = models.DateTimeField(auto_now=True) # 수정될 때 자동으로 넣어줌
    user = models.ForeignKey('users.MyUser', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="image", blank=True, null=True)


    def __str__(self):
        return f'제목 : {self.title} 내용 : {self.content}'
    

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 생성될 때 자동으로 넣어줌
    updated_at = models.DateTimeField(auto_now=True) # 수정될 때 자동으로 넣어줌
    user = models.ForeignKey('users.MyUser', on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.content}'