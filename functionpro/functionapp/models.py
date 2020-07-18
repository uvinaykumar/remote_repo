from django.db import models

# Create your models here.
class customer(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    company = models.CharField(max_length=10)
    mobile = models.BigIntegerField()
    loc = models.CharField(max_length=10)
    def __str__(self):
        return self.fname
