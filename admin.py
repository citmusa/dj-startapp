# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import SampleModel


@admin.register(SampleModel)
class SampleAdmin(admin.ModelAdmin):
    pass
