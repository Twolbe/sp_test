from django.db import models

# Create your models here.


class Request(models.Model):
    author = models.TextField(null=True, blank=True, verbose_name="request")
    phone = models.CharField(
        blank=True, null=True, max_length=100, verbose_name="phone"
    )

    class Meta:
        verbose_name = "request"
        verbose_name_plural = "reqests"
