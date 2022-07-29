from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from DimosoApp.models import *

# Register your models here.
class YourProfileAdmin(admin.ModelAdmin):
	list_display = ["true_name", "nick_name", "talent", "post_date"]
	#prepopulated_fields={'slug':('name',)}
class ChannelsLinkAdmin(admin.ModelAdmin):
	list_display = ["link","body","image","name", "post_date"]

admin.site.register(ChannelsLink, ChannelsLinkAdmin)
admin.site.register(YourProfile, YourProfileAdmin)