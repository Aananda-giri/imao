from django.urls import path


from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.Profile, name='profile'),
    path('uploadprofilepic/', views.UploadProfileView, name='upload_profile_pic'),
    path('categories/', views.categoriesView, name='categories'),
    path('info/', views.getUserDataView, name='info'),
    # ex: /polls/5/
    #path('<int:joke_id>/', views.detail, name='detail'),
]
