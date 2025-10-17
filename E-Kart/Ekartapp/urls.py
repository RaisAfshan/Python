from django.urls import path
from Ekartapp import views, admin_views, user_views

urlpatterns=[

#Views
    # path('',views.index,name='index'),
    path('Register',views.userRegisteration, name='Register1'),
    path('verify-otp',views.verify_otp_view,name='verify_otp'),
    path('login',views.loginUser,name='login1'),
    path('logout',views.logout_view,name='logout1'),


#Admin Views
    path('admin_dashboard',admin_views.admin_dashboard, name='adminDash'),

    #Category CRUD
    path('category_display',admin_views.categoryDisplay,name='categoryDisplay'),
    path('category_form',admin_views.category_view,name='categoryForm'),
    path('category_edit/<int:id>',admin_views.category_edit,name='categoryEdit'),
    path('category_delete/<int:id>',admin_views.category_delete,name='categoryDelete'),

    #Variant-type CRUD
    path('variant-display', admin_views.variant_type_view,name='variantDisplay'),
    path('variant-type-add',admin_views.variant_type_add,name='variantTypeAdd'),
    path('variant-type-edit/<int:id>',admin_views.variant_type_edit,name='variantTypeEdit'),
    path('variant-type-delete/<int:id>',admin_views.variant_type_delete,name='variantTypeDelete'),

    #Varinant CRUD
    path('variant-add',admin_views.variant_value_add,name='variantAdd'),
    path('variant-value-display',admin_views.variant_value_display,name='variantValueDisplay'),
    path('variant-value-edit/<int:id>',admin_views.variant_value_edit,name='variantValueEdit'),
    path('variant-value-delete/<int:id>',admin_views.variant_value_delete,name='variantValueDelete'),


    #Product CRUD
    path('product_display',admin_views.product_view,name='productDisplay'),
    path('product_add',admin_views.product_add,name='productAdd'),
    path('product_edit/<int:id>',admin_views.product_edit,name='productEdit'),
    path('product_delete/<int:id>',admin_views.product_delete,name='productDelete'),

    #Product Variant CRUD
    path('product_variant_display',admin_views.product_variant_display,name='productVariantDisplay'),
    path('product_variant_add/<int:id>',admin_views.product_variant_add,name='productVariantAdd'),
    path('product_variant_edit/<int:id>',admin_views.product_variant_edit,name='productVariantEdit'),
    path('product-varinat-delete/<int:id>',admin_views.product_variant_delete,name='productVariantDelete'),

    #Product Image CRUD
    path('product_image/<int:id>',admin_views.product_images_display,name='productImage'),
    path('image_add/<int:id>',admin_views.product_image_add,name='imageAdd'),
    path('image_edit/<int:id>',admin_views.product_image_edit,name='imageEdit'),
    path('image_delete/<int:id>',admin_views.product_image_delete,name='imageDelete'),


    #Product status
    path('order_status', admin_views.orderStatus, name='orderStatus1'),
    path('update-order-status/<int:id>',admin_views.update_order_status,name='updateOrderStatus'),
    path('order_status_edit/<int:id>',admin_views.order_edit,name='orderEdit1'),
    path('order_status_delete/<int:id>',admin_views.order_delete,name='orderStatusDelete'),

    #Admin Products Cards
    path('admin_products_overview',admin_views.admin_products_overview,name='adminProducts'),

    #User Admin
    path('admin_user', admin_views.admin_user_view,name='adminUser'),
    path('admin_user_edit/<int:id>',admin_views.admin_user_edit,name='adminUserEdit'),
    path('admin-user-delete/<int:id>',admin_views.user_delete,name='userDelete'),

    # Coupons
    path('coupons/', admin_views.coupon_list, name='coupon_list'),
    path('coupons/add/', admin_views.coupon_add, name='coupon_add'),
    path('coupons/edit/<int:id>/', admin_views.coupon_edit, name='coupon_edit'),
    path('coupons/delete/<int:id>/', admin_views.coupon_delete, name='coupon_delete'),

    #Banner
    path('banner_add',admin_views.add_banner,name='add_Banner'),
    path('banner_display',admin_views.banner_display,name='bannerDisplay'),
    path('banner_edit',admin_views.banner_edit,name='bannerEdit'),

    # Admin home page
    path('admin_home_page/',admin_views.admin_homepage,name='adminHomePage'),

# User Views
    path('user_home',user_views.user_home,name='userHome'),
    path('',user_views.user_productHome,name='userProductHome'),

    # Cart
    path('user_Cart', user_views.user_cart, name='userCart'),
    path('add-to-cart/<int:id>',user_views.add_to_cart,name='addToCart'),
    path('user-Coupons',user_views.couponsUser,name='userCoupons'),
    path('cart-update/<int:id> <str:action>',user_views.update_cart_quantity,name='update_cart_quantity'),
    path('apply-coupon',user_views.apply_coupon,name='applyCoupon'),

    # Product detail
    path('product-detail/<int:id>', user_views.product_detail, name='productDetail'),

    path('all-products',user_views.all_products, name='allProducts'),
    path('category-product',user_views.category_product , name='categoryProduct'),
    path('sub-category-product/<int:id>',user_views.sub_category_product , name='subCategoryProduct'),
    path('user-profile',user_views.user_profile, name='userProfile'),

    # Address
    path('user_address',user_views.user_address,name='userAddress'),
    path('user_address_post',user_views.user_postAddress,name='postAddress'),
    path('user-address-edit/<int:id>',user_views.updateAddress, name='userAddressEdit'),
    path('user-address-delete/<int:id>',user_views.deleteAddress,name='userDeleteAddress'),

    #Order
    path('user-Checkout',user_views.checkout_view,name='userCheckout'),
    path('user-proceedOrder',user_views.proceed_order_view,name='proceedOrder'),
    path('order-success/<int:id>',user_views.order_success_view,name='orderSuccess'),
    path('user-order-status-view',user_views.order_status,name='orderStatus'),
    path('change-address/', user_views.change_address, name='change_address'),







]