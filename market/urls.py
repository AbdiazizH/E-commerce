from django.urls import path, include
from . import views


urlpatterns = [ 
    # path('', views.home, name='all_products'),  
    path('', views.store, name='all_product'),  
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
]
     