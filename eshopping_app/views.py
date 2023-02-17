from django.core.paginator import Paginator, EmptyPage, InvalidPage

from django.shortcuts import render, get_object_or_404, redirect

from eshopping_app.models import categories_db, products_db


def eshop_home(request, cat_slug=None):
    pro_list = None
    cat_list = None
    if cat_slug is not None:
        cat_list = get_object_or_404(categories_db, slug=cat_slug)
        pro_list = products_db.objects.all().filter(category=cat_list, available=True)
    else:
        pro_list = products_db.objects.all().filter(available=True)
    paginator = Paginator(pro_list, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, 'shopping_home.html', dict(products=products, categories=cat_list))


def cat_add(request):
    category = categories_db.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', )
        details = request.POST.get('details', )
        image = request.FILES['image']
        category = categories_db(name=name, details=details, image=image)
        category.save()
        return redirect('e-shopping:eshop_home')
    return render(request, 'shopping_category_add.html', dict(category=category))


def eshop_products(request, cat_slug, pro_slug):
    try:
        product_details = products_db.objects.get(category__slug=cat_slug, slug=pro_slug)
    except Exception as e:
        raise e
    return render(request, 'shopping_products_details.html', dict(product=product_details))
