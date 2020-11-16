# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.


class jiangpin(models.Model):
    name = models.CharField('奖品名称',max_length=30,blank=True,help_text='奖品名称')
    user = models.CharField('获奖者',max_length=20,blank=True,help_text='获奖人')


class User(AbstractUser):
    count = models.IntegerField(verbose_name='抽奖次数')
    time = models.IntegerField(verbose_name='充值次数')