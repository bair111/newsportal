from django.contrib import admin
from .models import Author, Post, PostCategory, Comment, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'category', 'comment')
    list_filter = ('name', 'author', 'category')


admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Category)
