"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin, auth
# admin.autodiscover()

urlpatterns = [
	# IP(127.0.0.1:8000/admin)
    url(r'^admin/', admin.site.urls),
    # Uesr login 
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # User logout 设置登出之后的页面为根页面
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    # 将IP(127.0.0.1:8000/r'')对应的url设置为blog/urls.py中的urls
    url(r'', include('blog.urls'))
]


