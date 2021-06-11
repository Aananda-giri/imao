from django.urls import path


from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.chamber, name='chamber'),
    path('secrets/', views.secrets, name='secrets'),
    
    # ex: /polls/5/
#    path('<int:joke_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
#    path('<int:joke_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
#    path('<int:joke_id>/vote/', views.vote, name='vote'),
    
    
#    path('stupidstuff/', views.stupidstuff, name='stupidstuff'),
#    path('test/', views.test, name='test'),
#    path('taste/', views.taste, name='taste'),
#    path('ttaste/', views.ttaste, name='ttaste'),
#    path('uploadJokeView/', views.uploadJokeView, name='uploadJokeView'),
]

