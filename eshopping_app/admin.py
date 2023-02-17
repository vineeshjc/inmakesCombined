from django.contrib import admin

from eshopping_app.models import categories_db, products_db


class cat_adm(admin.ModelAdmin):
    list_display = ['name', 'slug', 'details', 'image']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(categories_db, cat_adm)


class pro_adm(admin.ModelAdmin):
    list_display = ['name', 'slug', 'details', 'image', 'price', 'stock', 'available', 'entered', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 5


admin.site.register(products_db, pro_adm)
