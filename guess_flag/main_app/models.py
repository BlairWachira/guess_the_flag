from django.db import models

class flags(models.Model):
    country_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='flags/')

    def __str__(self):
        return self.country_name
