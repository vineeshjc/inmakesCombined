from django.contrib import admin

from movies_app.models import movies_mod


class movies_admin(admin.ModelAdmin):
    list_display = ['name', 'story', 'released', 'image']


admin.site.register(movies_mod, movies_admin)
