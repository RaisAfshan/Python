from django.urls import path
from Ekartapp import views, admin_views, user_views

urlpatterns=[

#Views
    path('',views.index,name='index'),
    path('Register',views.userRegisteration, name='Register1'),
    path('login',views.loginUser,name='login1'),
    path('logout',views.logout_view,name='logout1'),


#Admin Views
    path('admin_dashboard',admin_views.admin_dashboard, name='adminDash'),

    #Category CRUD
    path('category_display',admin_views.categoryDisplay,name='categoryDisplay'),
    path('category_form',admin_views.category_view,name='categoryForm'),
    path('category_edit/<int:id>',admin_views.category_edit,name='categoryEdit'),
    path('category_delete/<int:id>',admin_views.category_delete,name='categoryDelete'),

    #Product CRUD
    path('product_display',admin_views.product_view,name='productDisplay'),
    path('product_add',admin_views.product_add,name='productAdd'),
    path('product_edit/<int:id>',admin_views.product_edit,name='productEdit'),
    path('product_delete/<int:id>',admin_views.product_delete,name='productDelete'),

    #Product Variant CRUD
    path('product_variant_display',admin_views.product_variant_display,name='productVariantDisplay'),
    path('product_variant_add',admin_views.product_variant_add,name='productVariantAdd'),
    path('product_variant_edit',admin_views.product_variant_edit,name='productVariantEdit'),
    #delete

    #Product Image CRUD
    path('product_image',admin_views.product_images_display,name='productImage'),
    path('image_add',admin_views.product_image_add,name='imageAdd'),
    path('image_edit',admin_views.product_image_edit,name='imageEdit'),


    #Product status
    path('order_status', admin_views.orderStatus, name='orderStatus1'),
    path('order_status_edit',admin_views.orderEdit,name='orderEdit1'),

    #Admin Products Cards
    path('admin_products_overview',admin_views.admin_products_overview,name='adminProducts'),

    #User Admin
    path('admin_user', admin_views.admin_user_view,name='adminUser'),

    #Banner
    path('banner_add',admin_views.add_banner,name='add_Banner'),
    path('banner_display',admin_views.banner_display,name='bannerDisplay'),
    path('banner_edit',admin_views.banner_edit,name='bannerEdit'),

    # Admin home page
    path('admin_home_page/',admin_views.admin_homepage,name='adminHomePage'),

# User Views
    path('user_home',user_views.user_home,name='userHome'),
    path('user_product_home',user_views.user_productHome,name='userProductHome'),
    path('user_Cart', user_views.user_cart, name='userCart')


]