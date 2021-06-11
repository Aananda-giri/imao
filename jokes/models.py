from django.db import models
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from user.models import User
import random
import string

#python3 manage.py migrate --database=jokes
#python3 manage.py migrate --fake
class Jokes(models.Model):
    #temporary_id = ...
    id = models.AutoField(primary_key=True)
    #id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))    # ascii_letters -> ascii_lowercase + ascii_uppercase
    
    #id = models.CharField(unique=True, primary_key=True, default=StringKeyGenerator(), editable=False)
    '''class StringKeyGenerator(object):
    def __init__(self, len=16):
        self.lenght = len
    def __call__(self):
        return ''.join(random.choice(string.letters + string.digits) for x in range(self.lenght))'''
    
    # Id assigned to joke in it's source website
    source = models.CharField(max_length = 100, default=None, null=True)
    source_id = models.IntegerField(default = None, null=True)
    
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=65000)
    author = models.CharField(max_length=100, default = None, null=True)
    loves = models.IntegerField(default=0)
    
    funney = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    rating_letters = models.CharField(max_length = 5)
    
    #rating_letterr = models.CharField(max_length = 5)
    #rrrating_letters = models.CharField(max_length = 5, default = None)
    
    #extract tags
    tags = ArrayField(models.CharField(max_length=150, blank=True), default=None, null=True)
    
    category = models.CharField(max_length=100,default=None, null=True)
    #tag = models.CharField(max_length=100, default='normal')
    shares = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    #read_content_ids = ArrayField(models.PositiveSmallIntegerField(null=True, blank=True), null=True, blank=True)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Create your models here.
#@login_required
class WockaJokes(models.Model):
    id = models. AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=65000)
    author = models.CharField(max_length=100)
    loves = models.IntegerField(default=0)
    funney = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    rating_letters = models.CharField(max_length = 5)
    #rating_letterr = models.CharField(max_length = 5)
    #rrrating_letters = models.CharField(max_length = 5, default = None)
    category = models.CharField(max_length=100)
    #tag = models.CharField(max_length=100, default='normal')
    shares = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    #read_content_ids = ArrayField(models.PositiveSmallIntegerField(null=True, blank=True), null=True, blank=True)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class StupidStuffJokes(models.Model):
    id = models. AutoField(primary_key=True)
    body = models.CharField(max_length=65000, default='')
    category = models.CharField(max_length=100, default='')
    rating = models.FloatField(default=0)
    title = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    loves = models.IntegerField(default=0)
    rating_letters = models.CharField(max_length = 5, default='' )
        #rating_letterr = models.CharField(max_length = 5)
    #rrrating_letters = models.CharField(max_length = 5, default = None)
    #tag = models.CharField(max_length=100, default='normal')
    shares = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    #read_content_ids = ArrayField(models.PositiveSmallIntegerField(null=True, blank=True), null=True, blank=True)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class RedditJokes(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    body = models.CharField(max_length=50000, default='')
    #category = models.CharField(max_length=100, default='')
    score = models.FloatField(default=0)
    title = models.CharField(max_length=350, default='')
    #author = models.CharField(max_length=100, default='')
    loves = models.IntegerField(default=0)
    #rating_letters = models.CharField(max_length = 5, default='' )
        #rating_letterr = models.CharField(max_length = 5)
    #rrrating_letters = models.CharField(max_length = 5, default = None)
    #tag = models.CharField(max_length=100, default='normal')
    shares = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    #read_content_ids = ArrayField(models.PositiveSmallIntegerField(null=True, blank=True), null=True, blank=True)
    def __str__(self):
        return (str(self.title) + '  \n' +  str(self.body))
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class UploadJokes(models.Model):
    id = models.AutoField(primary_key=True);
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=5000)
    category = models.CharField(max_length=100, default=None, null=True)
    votes = models.IntegerField(default=0)
    #rating = models.FloatField(default=0)
    tag = models.CharField(max_length=100, default=None, null=True)
    shares = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    def __str__(self):
        return(self.title + ':\n\t' + self.body)
        
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class SearchModel(models.Model):
    search_term = models.CharField(max_length=100)

'''class RedditJokes(models.Model):

    joke_title = models.CharField(max_length=100)
    def __str__(self):
        return self.joke_title'''


class Comments(models.Model):
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    
    # UploadJokes as foreign Key for real Implications
    wockajokes = models.ForeignKey(WockaJokes, on_delete=models.CASCADE)
    
    body = models.CharField(max_length=150, default = None)
    loves = models.IntegerField(default=0)
    
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

    

class ShortedList(models.Model):
    category = models.CharField(max_length=100, primary_key = True)
    shortedids = ArrayField(models.PositiveSmallIntegerField(null=True, blank=True), null=True, blank=True)
#ArrayField(models.CharField(max_length=250, blank=True), default=None, null=True)

class AbsurdlyBigJokes(models.Model):
    id = models. AutoField(primary_key=True)
    category = models.CharField(max_length=100, default = '')
    title = models.CharField(max_length=100, default = '')
    body = models.CharField(max_length = 2500)
    author = models.CharField(max_length=100, default = '')
    loves = models.IntegerField(default=0)
    funney = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    rating_letters = models.CharField(max_length = 5)
    #rating_letterr = models.CharField(max_length = 5)
    #rrrating_letters = models.CharField(max_length = 5, default = None)
    #tag = models.CharField(max_length=100, default='normal')
    shares = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    #read_content_ids = ArrayField(models.PositiveSmallIntegerField(null=True, blank=True), null=True, blank=True)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

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
        
