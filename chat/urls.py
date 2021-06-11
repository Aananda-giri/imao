from django.urls import path


from . import views

urlpatterns = [
    # ex: /polls/
    path('',views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('not_available', views.chat, name='chat'),
]
