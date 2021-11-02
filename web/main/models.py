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


<<<<<<< HEAD
# Create your models here.
class g_menu(models.model):
    menu_item = models.CharFild(max_lent)
    aa = forms.BooleanField(aa, required=False)
    FIELDNAME = forms.CharField(, max_length=, required=False)
    
=======
>>>>>>> 07ec04e3a3e87e1683c8a5c6cb0aae2dff183abe
