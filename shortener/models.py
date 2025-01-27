from django.db import models

class URLMapping(models.Model):
    original_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.original_url
