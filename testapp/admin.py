from django.contrib import admin
from testapp.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['id','User_Name','User_Pwd']

admin.site.register(User,UserAdmin)
