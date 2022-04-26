from django.urls import reverse
from django.shortcuts import render

MENU_LINCS = {
    'index': 'Главная',
    'products': 'Продукты',
    'contact': 'Контакты',
}


def main(request):
    return render(request, "mainapp/index.html", context= {
        'title': 'Главная',
        'menu': MENU_LINKS,
    })

def products(request):
    return render(request, "mainapp/products.html", context= {
        'title': 'Продукты',
        'menu': MENU_LINKS,
    })


def contact(request):
    return render(request, "mainapp/contact.html", context= {
        'title': 'Контакты',
        'menu': MENU_LINKS,
    })
    