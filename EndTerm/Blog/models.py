from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    createdAt = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title
