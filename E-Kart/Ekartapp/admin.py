from django.contrib import admin

from Ekartapp.models import Custom_User, UserModel, Category, Product


# Register your models here.

class AdminCustomUser(admin.ModelAdmin):
    pass

class AdminUser(admin.ModelAdmin):
    list_display = ('user', 'fullName', 'phoneNumber', 'gender', 'profilePicture', 'email', 'created_at')

class AdminCategory(admin.ModelAdmin):
    list_display = ('name','parent')

class AdminProduct(admin.ModelAdmin):
    list_display = ('created_by','brand','title','description','price','category')


admin.site.register(Custom_User)
admin.site.register(UserModel,AdminUser)
admin.site.register(Category,AdminCategory)
admin.site.register(Product,AdminProduct)
