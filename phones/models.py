from django.db import models
from slugify import slugify


class Phone(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    def slug(self):
        return str(slugify(self.name))

