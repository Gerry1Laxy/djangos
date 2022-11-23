from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {
        'phones': None
    }
    sort = request.GET.get('sort')
    if not sort:
        context['phones'] = Phone.objects.all()
    else:
        if sort == 'name':
            context['phones'] = Phone.objects.order_by(sort)
        elif sort == 'min_price':
            context['phones'] = Phone.objects.order_by('price')
        elif sort == 'max_price':
            context['phones'] = Phone.objects.order_by('-price')
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)
