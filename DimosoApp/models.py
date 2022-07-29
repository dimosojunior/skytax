from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class ChannelsLink(models.Model):

    name = models.CharField(max_length=200, blank=True, null=True)
    song_name = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=1000, blank=True, null=True)
    
    
    
    body = models.CharField(max_length=200,blank=True, null=True)
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(max_length=200,blank=True, null=True, upload_to="media/")

class YourProfile(models.Model):
    true_name = models.CharField(max_length=200, blank=True, null=True)
    nick_name = models.CharField(max_length=200, blank=True, null=True)
    
    
    
    talent = models.CharField(max_length=200,blank=True, null=True)
    
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/")
    