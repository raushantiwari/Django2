from django import forms
from blogs.models import Blogs


class BlogsForm(forms.ModelForm):
    class Meta:
        model = Blogs
        # fields = '__all__'
        fields = ['title', 'image', 'body', 'blog_category', 'published']
