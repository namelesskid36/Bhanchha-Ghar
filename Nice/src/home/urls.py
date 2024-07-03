from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
   path('', views.index, name='home'), 
   path('ContactUs/', views.show_contactus, name='ContactUs'),
   path('Users/', views.show_product, name='show_product'),
   path('Chefs/', views.show_productBroker, name='show_productBroker'),
   path('Login/', views.show_login, name='login'),
   path('Register/', views.show_selectRegister, name='selectregister'),
   path('ChefRegister/', views.show_registerBroker, name='registerbroker'),
   path('UserRegister/', views.show_registerRegular, name='registerregular'),
   path('LoginSuccess/', views.show_successLogin, name='successLogin'),
   path('EMVUsers/', views.verify_emailregular, name='verify_emailregular'),
   path('EMVChefs/', views.verify_emailbroker, name='verify_emailbroker'),
   path('logout/', views.show_logout, name='logout'),
   path('AddProfile/', views.show_AddProduct, name='AddProduct'),
   path('MyProfile/', views.show_MyProduct, name='MyProduct'),
   path('Profile/', views.show_profile, name='profile'),
   path('UpdateProfile/', views.update_profile, name='updateprofile'),
   path('ChefsProfile/', views.show_Food, name='Foods'),
   path('Chef/<int:chef_id>/', views.product_detail, name='product_detail'),
   path('updateprofile/<int:chef_id>/', views.show_updateProduct, name='updateproduct'),
   path('deleteprofile/<int:chef_id>/', views.show_deleteProduct, name='deleteProduct'),
   path('Recipies/', views.recipie, name='recipie'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)