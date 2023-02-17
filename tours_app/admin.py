from django.contrib import admin
from django.contrib.admin import site

from tours_app.models import banner_back, header_back, footer_back, our_tours, our_team

class header_adm(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']

admin.site.register(header_back, header_adm)

class banner_adm(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']

admin.site.register(banner_back, banner_adm)

class footer_adm(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']

admin.site.register(footer_back, footer_adm)


class team_adm(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']

admin.site.register(our_team, team_adm)


