from django.contrib import admin
from .models import Post, Comment
# models.py里面写出的类 在此注册
# 如果要想将写出的类反映到admin 就一定要注册
admin.site.register(Post)
admin.site.register(Comment)