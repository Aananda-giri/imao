from django.urls import path


from . import views

urlpatterns = [
    # ex: /polls/
    #path('<int:joke_page>/', views.index, name='jokes_with_page_no'),
    path('', views.index, name='jokes'),
    # ex: /polls/5/
    #path('<int:joke_id>/', views.joke_by_id, name='joke_by_id'),
    # ex: /polls/5/results/
    path('<int:joke_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:joke_id>/vote/', views.vote, name='vote'),
    
    
    path('stupidstuff/', views.stupidstuff, name='stupidstuff'),
    path('test/', views.test, name='test'),
    path('taste/', views.taste, name='taste'),
    path('ttaste/', views.ttaste, name='ttaste'),
    path('uploadJokeView/', views.uploadJokeView, name='uploadJokeView'),
    
    #path('feedback/', views.sendMail, name='sendmail'),
    path('feedback/', views.feedback, name='feedback'),
    
    path('get/jokes/', views.getJoke, name='get_jokes'),
    path('vote', views.vote, name='vote'),
    
    path('comments', views.getComments, name='comments'),
    path('savecomment', views.saveComment, name='savecomment'),
    path('save_new_jokes_comment', views.saveNewJokesComment, name='save_new_jokes_comment'),
    
    
    
    path('<int:joke_id>/', views.each_joke, name='first_template'),
    path('category/', views.get_category, name = 'get_category'),
    path('category/<str:category>/', views.get_category, name = 'get_category'),
    path('joke_api/', views.random_joke_api, name = 'api/random'),
]



