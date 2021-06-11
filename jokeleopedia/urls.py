"""jokeleopedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# For user authentication (login/logout)
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView 
from jokes.views import vote as j, index

from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap, LoginViewSitemap, EachJokes

sitemaps = {
    'static': StaticViewSitemap,
    'login':LoginViewSitemap,
    'each_jokes':EachJokes,
}

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jokes/', include('jokes.urls')),
    path('vote/', j, name='vote'),
    #path('ariesap', include('ariesap.urls')),
    #path('memmes/', include('memmes.urls')),
    path('', include('memes.urls')),
    path('user/', include('user.urls')),
    #path('searchtest/', include('searchtest.urls')),
    path('register/', views.Join, name='join'),    
    path('login/', auth_views.LoginView.as_view(), name='Login'),
    #path('register/', auth_views.RegisterView.as_view(), name='Register'),
    path('logout/', auth_views.LogoutView.as_view(), name='Logout'),
    
    #path('category/', views.categories, name='category'),
    
    #path('accounts/password_reset/done/', name='password_reset_done'),
    #path('password_change/', auth_views.PasswordChangeView.as_view(), name='logout'),
    #path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('home', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', index, name='index'),
    path('chit-chat/', include('chat.urls')),
    path('cos/',include('cos.urls')),
    path('tu/',include('hotornot.urls')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
]




#The URLs provided by auth are:
'''
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
Source:https://learndjango.com/tutorials/django-login-and-logout-tutorial
'''
