from django.db import models
from django.contrib.sites.models import Site


class SiteScheme(models.Model):
    SCHEMES = (
        ('http', 'http'),
        ('https', 'https'),
    )
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    scheme = models.CharField(max_length=10, choices=SCHEMES, default='https')
