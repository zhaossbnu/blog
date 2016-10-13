from django.conf.urls import url
from . import views

urlpatterns = [
	# 列出所有对象的网页url
	url(r'^$', views.post_list, name = 'post_list'),
	# 新建一个post的网页url
	url(r'^post/new/$', views.post_new, name='post_new'),
	# 修改表单
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	# 查看一个post详细信息的url
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	# 查看草稿
	url(r'^draft/$', views.post_draft_list, name = 'post_draft_list'),
	# publish one post
	url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name = 'post_publish'),
	# Remove one post
	url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name = 'post_remove'),
	# add comment
	url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name = 'add_comment_to_post'),
	# approve comment
	url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name = 'comment_approve'),
	# remove comment
	url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name = 'comment_remove'),
]