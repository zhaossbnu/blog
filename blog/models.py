from django.db import models
from django.utils import timezone
# 在此内部定义APP中的类 对应数据库中的表
# 博客
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approve_comment = True)

    def __str__(self):
        return self.title
# 评论
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    approve_comment = models.BooleanField(default = False)

    def approve(self):
        self.approve_comment = True
        self.save()
        
    def __str__(self):
        return self.text