from django.db import models

# Create your models here.
# TIP: commands
# python manage.py makemigrations
# python manage.py migrate

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #add in thumbnail later
    #add author later