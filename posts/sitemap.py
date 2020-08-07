from django.contrib.sitemaps import Sitemap
from .models import Post


class BlogSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.7

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.timestamp
