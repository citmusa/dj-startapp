# -*- coding: utf-8 -*-
from django.db import models


class SampleModel(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'sample'

    def __str__(self):
        return self.title
