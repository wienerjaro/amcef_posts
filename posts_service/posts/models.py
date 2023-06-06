from django.db import models


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField(blank=False, null=False)
    title = models.CharField(blank=False, null=False, max_length=255)
    body = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title
