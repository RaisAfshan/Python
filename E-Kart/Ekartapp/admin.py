from django.contrib import admin

from Ekartapp.models import Custom_User, UserModel, Category, Product, VariantType, Variants, ProductVariant, \
    ProductVariantImage


# Register your models here.

class AdminCustomUser(admin.ModelAdmin):
    pass

class AdminUser(admin.ModelAdmin):
    list_display = ('user', 'fullName', 'phoneNumber', 'gender', 'profilePicture', 'email', 'created_at')

class AdminCategory(admin.ModelAdmin):
    list_display = ('name','parent')

class AdminProduct(admin.ModelAdmin):
    list_display = ('created_by','brand','title','description','category')

class AdminVariantType(admin.ModelAdmin):
    list_display = ('name',)

class AdminVariants(admin.ModelAdmin):
    list_display = ('variant_type','value')

class AdminProductVariants(admin.ModelAdmin):
    list_display = ('product','primary_variant','secondary_variant','price','quantity','is_default','created_at')

class AdminProductImage(admin.ModelAdmin):
    list_display = ('product_variant','image','is_default')

admin.site.register(Custom_User)
admin.site.register(UserModel,AdminUser)
admin.site.register(Category,AdminCategory)
admin.site.register(Product,AdminProduct)
admin.site.register(VariantType,AdminVariantType)
admin.site.register(Variants,AdminVariants)
admin.site.register(ProductVariant,AdminProductVariants)
admin.site.register(ProductVariantImage,AdminProductImage)
