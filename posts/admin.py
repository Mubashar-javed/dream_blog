from django.contrib import admin

from .models import Author, Category, Post, Comment, PostView
from django.contrib.contenttypes.models import ContentType


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = (('user', 'profile_picture'),)


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
