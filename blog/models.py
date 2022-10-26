from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(default='defaultslug')
    content=models.TextField()
    # auto now add adds when the post was created
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class Comment(models.Model):
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)

    # somehow acess the post for which this is being saved
    def save(self):
        ...