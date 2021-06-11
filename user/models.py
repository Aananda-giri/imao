
from django.db import models
#from django.db import PositiveBigIntegerField

# Create your models here.
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.fields import ArrayField
import uuid

#######////////////////// Ommit Comment \\\\\\\\\\\\\\\#########  
#@login_required
class ProfilePicModel(models.Model):
    image = models.FileField(upload_to='user/static/user/profile_pics')
    pub_date = models.DateTimeField('date published', default=timezone.now)

#######////////////////// Ommit Comment \\\\\\\\\\\\\\\#########  
#@login_required
class User(models.Model):
    username = models.CharField(max_length = 50, primary_key=True)#one to one key with request.user.username
    first_name = models.CharField(max_length = 50, default=None, null=True)
    middle_name = models.CharField(max_length = 50, default=None, null=True)
    last_name = models.CharField(max_length = 50, default=None, null=True)
    preferred_categories = ArrayField(models.CharField(max_length=250, blank=True), default=None, null=True)
    email = models.EmailField()
    her_country = models.CharField(max_length=60, default = None, null=True)
    phone_number = models.BigIntegerField(default=0,)
    relligion = models.CharField(max_length = 50)
    profile_url = models.CharField(max_length = 100, default='')
    profile_pic = models.FileField(upload_to='user/static/user/images',null=True)

class ModelWithFileField(models.Model):
    title = models.CharField(max_length=50)
    filez = models.FileField(upload_to='jokes/static/jokes/images')
    #class Mete:
     #   db_table='chuckles'

'''
Post is the name of model
>>> Post.objects.create(name='Third post', tags=['tutorial', 'django'])

>>> Post.objects.filter(tags__contains=['thoughts'])'''
