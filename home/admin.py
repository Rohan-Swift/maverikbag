from django.contrib import admin

# Register your models here.
from home.models import Counting, Volunteer, Pay, Email, Image, TeamPic


class AdminEmail(admin.ModelAdmin):
    list_display = ['email']

class AdminPay(admin.ModelAdmin):
    list_display = ['img']


class AdminCounting(admin.ModelAdmin):
    list_display = ['volunteer', 'event']


class AdminVolunteer(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Counting, AdminCounting)
admin.site.register(Volunteer, AdminVolunteer)
admin.site.register(Pay, AdminPay)
admin.site.register(Email, AdminEmail)
admin.site.register(Image)
admin.site.register(TeamPic)
