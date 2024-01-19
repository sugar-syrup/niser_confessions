from django.db import models


class ConfessionModel(models.Model):
    from_name = models.CharField(max_length=128)
    to_name = models.CharField(max_length=128)
    confession = models.TextField(max_length=2040)
