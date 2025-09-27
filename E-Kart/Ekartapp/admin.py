from django.contrib import admin

from Ekartapp.models import Custom_User, UserModel


# Register your models here.

class AdminCustomUser(admin.ModelAdmin):
    pass

class AdminUser(admin.ModelAdmin):
    list_display = ('user', 'fullName', 'phoneNumber', 'gender', 'profilePicture', 'email', 'created_at')
admin.site.register(Custom_User)
admin.site.register(UserModel,AdminUser)