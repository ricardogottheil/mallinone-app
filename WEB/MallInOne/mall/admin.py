# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Mall

@admin.register(Mall)
class MallAdmin(admin.ModelAdmin):
    list_display=('name',)
    list_display_links= ('name',)
    empty_value_display = '-????-'



# admin.site.register(Mall)