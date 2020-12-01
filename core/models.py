from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(null=True, blank=True)
    street_address = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    postcode = models.IntegerField()

    def __str__(self):
        return self.name
