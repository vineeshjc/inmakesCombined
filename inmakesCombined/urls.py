
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('directory/', include('register_app.urls')),
    path('travel/', include('tours_app.urls')),
    path('movies/', include('movies_app.urls')),
    path('todo/', include('todo_app.urls')),
    path('todo_cv/', include('todo_list_view_app.urls')),
    path('e-shopping/', include('eshopping_app.urls')),
    path('e-search/', include('eshopping_search.urls')),
    path('cart/', include('eshopping_cart_app.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)