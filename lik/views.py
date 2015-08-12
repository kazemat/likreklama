from django.shortcuts import render
from .models import Category, Product
from cms.models import TextBlock, Contacts
from django.http import Http404


def index(request, param=None):
    text = TextBlock.objects.filter(name='main').first()
    return render(request, 'layout.html', dict(
        title_lg='Главная',
        text=text
    ))


def about(request):
    text = TextBlock.objects.filter(name='about').first()
    return render(request, 'pages/simple.html', dict(
        title_lg='О нас',
        text=text
    ))


def contacts(request):
    text = Contacts.objects.first()
    print(text)
    return render(request, 'pages/contacts.html', dict(
        title_lg='Контакты',
        text=text
    ))


def product_from_category(request, cat_id):
    params = list(map(
        lambda x: int(x),
        request.path.strip('/').split('/')
    ))
    cat_id = params[0]
    category = Category.objects.filter(id=cat_id).first()
    if category is None:
        raise Http404
    product = Product.objects.filter(category__id=cat_id)
    if len(params) == 2:
        product_id = params[1]
        product = product.filter(id=product_id)
    product = product.first()
    all = Product.objects.filter(category__id=cat_id).order_by('date_add').all()
    request.session['category'] = cat_id
    return render(request, "pages/product.html", dict(
        title_lg=category.name,
        title_sm=product.name,
        product=product,
        all=all,
        cat_id=cat_id
    ))
