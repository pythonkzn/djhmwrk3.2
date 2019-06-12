from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort == 'name':
        phones = sorted(phones, key=lambda k: k.name)
    elif sort == 'min_price':
        phones = sorted(phones, key=lambda k: k.price)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.all()
    context = {}
    for phone in phones:
        if phone.slug() == slug:
            context = {'phone': phone}
    return render(request, template, context)
