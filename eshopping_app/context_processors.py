from eshopping_app.models import categories_db


def links_menu(request):
    links = categories_db.objects.all()
    return dict(links=links)