# from django import forms
# from blogs.models import Blogs
#
#
# class BlogsForm(forms.ModelForm):
#     class Meta:
#         model = Blogs
#         # fields = '__all__'
#         fields = ['title', 'image', 'body', 'summary', 'blog_category', 'published']

from django.forms import ModelForm
from .models import Blogs


class BlogsForm(ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'image', 'body', 'summary', 'summary1', 'blog_category', 'published']
