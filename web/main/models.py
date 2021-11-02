from django.db import models

class smenu(models.Model):
    

    class Meta:
        verbose_name = ("მენიუ")
        verbose_name_plural = ("მენიუ")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("smenu_detail", kwargs={"pk": self.pk})
