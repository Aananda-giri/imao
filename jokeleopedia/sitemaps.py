# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from jokes.models import WockaJokes

'''class BlogPostSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return WockaJokes.objects.all()'''

class StaticViewSitemap(Sitemap):
    changefreq = 'daily'
    priority=1

    def items(self):
        return ['jokes', 'imgflip_memes']

    def location(self, item):
        return reverse(item)
    
    def lastmod(self, obj):
        return obj.pub_date
