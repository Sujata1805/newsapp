from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.
