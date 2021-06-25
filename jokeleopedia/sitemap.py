# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
#from jokes.models import WockaJokes

'''class BlogPostSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return WockaJokes.objects.all()'''

class StaticViewSitemap(Sitemap):
    changefreq = 'daily'
    priority=1
    protocol = 'https'

    def items(self):
        return ['jokes', 'imgflip_memes']

    def location(self, item):
        print('\n\n\nreturning_from_sitemaps:\n\n'+str(reverse(item)))
        return reverse(item)


class LoginViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6
    protocol = 'https'

    def items(self):
        return ['feedback', 'memes_feedback', 'login', 'logout', 'join']

    def location(self, item):
        return reverse(item)

class EachJokes(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return [i for i in range(0, 15480)] # that are the number of jokes available.

    def location(self, item):
        return('/jokes/'+str(item)+'/')

#Source:https://www.ordinarycoders.com/blog/article/django-sitemap
