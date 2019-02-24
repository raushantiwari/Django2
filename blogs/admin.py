from django.contrib import admin
from .models import Blogs


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'pub_date', 'published']
    list_filter = ('author', 'pub_date')
    # fields = [('title', 'body'), ('author', 'pub_date'), ('image', 'delete'), ('published'), ]
    fieldsets = (
        ('Section 1', {
            'fields': ('title', 'body')
        }),
        ('Section 2', {
            'fields': ('image', 'blog_category')
        }),
        ('Section 3', {
            'fields': ('author', 'pub_date', 'published')
        }),
    )


admin.site.register(Blogs, BlogAdmin)
