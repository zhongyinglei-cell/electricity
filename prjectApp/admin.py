# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from prjectApp.models import User
# Register your models here.
# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
