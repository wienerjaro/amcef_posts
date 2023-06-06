from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'title', 'body')  # List of fields to display in the admin list view


admin.site.register(Post, PostAdmin)
