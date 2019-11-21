from django.contrib import admin
from .models import Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['comment_name', 'comment_email', 'url', 'article','text', 'created_time']
    fields = ['comment_name', 'comment_email', 'url', 'text', 'article']


admin.site.register(Comments, CommentsAdmin)