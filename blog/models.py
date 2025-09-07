from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return f"{self.title[:20]} | {self.content[:30]}... Written by: {self.author} | Created at: {self.created_at}"
