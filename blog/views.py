from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from .models import Post, Comment
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import os
# 将模型中的数据传递给模板
# 这一部分很重要 相当于是一座桥
# Create your views here

# 列出所有博客
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 将刚查询得到的posts以模板标签的形式传递给网页
	return render(request, 'blog/post_list.html', {'posts':posts})

# 单独显示一个博客
def post_detail(request, pk):
    # 通过主键来获得一片博客的详细信息
    post = get_object_or_404(Post, pk = pk)
    # 将刚查询得到的posts以模板标签的形式传递给网页
    return render(request, 'blog/post_detail.html', {'post': post})

# 新建一个博客
@login_required
def post_new(request):
    # 表单中所有的数据都在request.POST
    if request.method == "POST":
        # 用表单里面的东西构建PostForm
        form = PostForm(request.POST)
        if form.is_valid():
            # commit=False意味着我们还不想保存Post模型
            post = form.save(commit = False)
            # 设置请求者为作者
            post.author = request.user
            # post.published_date = timezone.now()
            # 保存表单
            post.save()
            # 编写完之后 将网页指向单独显示一个博客的地方
            return redirect('blog.views.post_detail', pk = post.pk)
    else:
        # 第一次访问得到一个空表单
        form = PostForm()
    # 到编辑界面
    return render(request, 'blog/post_edit.html', {'form': form})
    
# 修改一个博客
@login_required
def post_edit(request, pk):
    # 得到一个博客
    post = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        # 用得到的博客构建一个PostForm
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk = post.pk)
    else:
        # 第一次访问 
        form = PostForm(instance = post)
    # 到编辑界面
    return render(request, 'blog/post_edit.html', {'form': form})

# show draft
@login_required
def post_draft_list(request):
    # 查询未发布的博客
    posts = Post.objects.filter(published_date__isnull = True).order_by('created_date')
    # 将刚查询得到的posts以模板标签的形式传递给网页
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

# publish draft
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.published_date = timezone.now()
    post.save()
    return redirect('blog.views.post_detail', pk = post.pk)
    
# delete 
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.delete()
    return redirect('blog.views.post_list')

# add comments
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.comment_approve = False
            comment.save()
            return redirect('blog.views.post_detail', pk = post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form':form})

# approve comment
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk = comment.post.pk)

# remove comment
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    # 设置临时变量为删除的评论所处的博客 因为以后会用到
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk = post_pk)

