from django.urls import path

from . import views

app_name = 'e-shopping'

urlpatterns = [
    path('eshop_home', views.eshop_home, name='eshop_home'),
    path('<slug:cat_slug>/', views.eshop_home, name='cat_pro'),
    path('cat_add', views.cat_add, name='cat_add'),
    path('<slug:cat_slug>/<slug:pro_slug>/', views.eshop_products, name='eshop_products'),
]
