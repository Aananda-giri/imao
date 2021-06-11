from django.urls import path


from . import views

urlpatterns = [
    # ex: /polls/
    path('index', views.index, name='index'),
    path('home/', views.viewMemes, name='viewMemes'),
    path('upload/', views.toImagur, name='toImagur'),
    path('u/', views.upload, name='upload'),
    path('default/', views.memes, name='memes'),
    path('', views.ImgflipMemes, name='imgflip_memes'),
    path('get_memes/', views.getMeme, name='get_memes'),
    # ex: /polls/5/
    #path('<int:joke_id>/', views.detail, name='detail'),
    
    #for increasing/decreasing votes
    path('vote/', views.vote, name='vote_meme'),
    
    #for getting list of comments
    path('get_comments/', views.getComments, name='meme_comments'),
    
    #for saving new comments
    path('save_comment/', views.saveComment, name='save_meme_comment'),
    path('feedbacks/', views.feedback, name='memes_feedback'),
    
    path('sitemap/', views.sitemap, name='sitemap'),
    
]
