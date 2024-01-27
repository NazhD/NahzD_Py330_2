from django.db import models


class ListTexter(models.Model):
    type_texter = models.CharField(max_length=20)
    name_texter = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='list/images/')
    url = models.URLField(blank=True)
