from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    # auto now add adds when the post was created
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title