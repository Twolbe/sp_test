from django.db import models

class BannerTypeChoices(models.TextChoices):
    COMBO = "combo"
    WEB_VIEW = "web_view"
    PRODUCT = "product"
    INFO = "info"

class Banner(models.Model):
    image = models.TextField(null=False, blank=False, verbose_name="image")
    banner_type = models.CharField(
        blank=False, 
        null=False, 
        max_length=10, 
        verbose_name="banner_type",
        choices=BannerTypeChoices.choices,
    )

    class Meta:
        verbose_name = "banner"
        verbose_name_plural = "banners"