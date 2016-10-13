from django import forms
from .models import Post, Comment
# 表单
# 也就是用户填写/修改博客的一个模式
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text', )

# 评论的表单模式
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('author', 'text', )