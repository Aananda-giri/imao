from django.db import models

import datetime
from django.utils import timezone
from user.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class UploadMeme(models.Model):
    user=models.ForeignKey(User, to_field='username', on_delete=models.CASCADE, default='her')
    meme = models.FileField(upload_to='memes/static/memes/images')
    pub_date = models.DateTimeField('date published', default=timezone.now)
    title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=500, default='')
    url = models.CharField(max_length=100, default='')

class Meme(models.Model):
    id = models.AutoField(primary_key=True)
    #category = models.CharField(max_length=50)
    imgflip_type = models.CharField(max_length=100, default='')
    imgflip_url = models.CharField(max_length=300, default='')
    imgflip_post = models.CharField(max_length=300, default='')
    imgflip_views = models.PositiveIntegerField(default=0, null=True)
    imgflip_img_votes = models.IntegerField(default=0, null=True)
    imgflip_title = models.CharField(max_length = 300, default='', null=True)
    imgflip_author = models.CharField(max_length = 150, default='', null=True)
    imgflip_boxes = ArrayField(models.CharField(max_length=200, blank=True), default=None, null=True)
    
    loves = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    rating_letters = models.CharField(max_length = 5, default='')
    languages = ArrayField(models.CharField(max_length=30, blank=True), default=None, null=True)
    
    #author = models.CharField(max_length=100)
    #rating_letterr = models.CharField(max_length = 5)
    #rrrating_letters = models.CharField(max_length = 5, default = None)
    #title = 
    
    pub_date = models.DateTimeField('date published',default=timezone.now)
    #read_content_ids = ArrayField(models.PositiveSmallIntegerField(null=True, blank=True), null=True, blank=True)
    def __str__(self):
        return str(self.imgflip_type)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#to be implemented using --database = imgflip_memes
class ImgflipMemes(models.Model):
    #id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    loves = models.IntegerField(default=0)
    
class MemesComments(models.Model):
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    meme = models.ForeignKey(ImgflipMemes, on_delete=models.CASCADE)
        
    # UploadJokes as foreign Key for real Implications
    meme_position = models.IntegerField(default=0)
    
    body = models.CharField(max_length=150, default = '')
    loves = models.IntegerField(default=0)
    #id = models.IntegerField(primary_key=True)
    
    def __str__(self):
        return self.body
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def appendReadIds():
        print('I want')

    def incrementCommentVote(id):
        print('I want')

    def incrementCommentVote(id):
        print('I want')


#python3 manage.py migrate --database=feedbacks
class Feedbacks(models.Model):
    username = models.CharField(max_length=50, default = None, null=True)
    body = models.CharField(max_length=500, default = None)
    loves = models.IntegerField(default=0)    
    email = models.EmailField(default = None,)
    
    pub_date = models.DateTimeField('date published',default=timezone.now)
    def __str__(self):
        return('Username: {}, Body:{}, email:{}'.format(self.username, self.body, self.email))
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
