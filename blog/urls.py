from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.flatpages import views as flat_views

from marketing.views import email_list_signup
from django.contrib.sitemaps.views import sitemap
from posts.sitemap import BlogSiteMap

sitemaps = {
    'sitemap': BlogSiteMap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('email-signup/', email_list_signup, name='email-list-signup'),

    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),

    path('pages/', include('django.contrib.flatpages.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
