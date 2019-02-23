from django.db import models


# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    delete = models.IntegerField(default=0)
    published = models.BooleanField(default=True)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def pretty_text(self):
        return self.body[:100]

    class Meta:
        db_table = 'blogs'
