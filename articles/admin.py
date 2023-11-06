from django.contrib import admin
from .models import *

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)