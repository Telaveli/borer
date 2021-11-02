from django.db import models
from django.db.models.fields import IntegerField

class smenu(models.Model):
    mname = models.CharField("სახელი", max_length=20)
    level = models.IntegerField("დონე", default=0)
    hkey = models.BigIntegerField("კოდი")

    class Meta:
        verbose_name = ("Menu")
        verbose_name_plural = ("Memus")

    def __str__(self):
        return self.mname


