from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(db_index=True, max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    body = models.TextField()
    summary = RichTextUploadingField(blank=True, null=True)
    # summary = RichTextField(blank=True, null=True)
    published = models.BooleanField(default=True)
    BLOG_CATEGORY_CHOICES = (
        ('Political', 'Political'),
        ('Movies', 'Movies'),
        ('World War', 'World War'),
    )
    blog_category = models.CharField(
        max_length=25,
        choices=BLOG_CATEGORY_CHOICES,
        default='World War',
        db_index=True,
    )
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
    
    def pretty_text(self):
        return self.body[:100]
    
    class Meta:
        db_table = 'blog'
