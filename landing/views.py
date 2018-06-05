from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *


def landing(request):
    name = "Человек"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print (data["name"])
        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_akusticheskieudarnye = products_images.filter(product__category__id=3)
    products_images_ehlektronnyeudarnye = products_images.filter(product__category__id=4)
    products_images_instrumentysmembranoj = products_images.filter(product__category__id=5)
    products_images_samozvuchashchieinstrumenty = products_images.filter(product__category__id=6)
    # products_images_chekhlykejsysumki  = products_images.filter(product__category__id=7)
    # products_images_metronomyipriborynastrojki = products_images.filter(product__category__id=8)
    products_images_zapchastiikomplektuyushchie = products_images.filter(product__category__id=9)
    products_images_barabannyepalochkiishchyotki = products_images.filter(product__category__id=10)
    return render(request, 'landing/home.html', locals())


def contacts(request):
    return render(request, 'landing/contacts.html', locals())


def checkout(request):
    return render(request, 'orders/checkout.html', locals())


def akusticheskieudarnye(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_akusticheskieudarnye = products_images.filter(product__category__id=3)
    return render(request, 'landing/akusticheskieudarnye.html', locals())


def ehlektronnyeudarnye(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_ehlektronnyeudarnye = products_images.filter(product__category__id=4)
    return render(request, 'landing/ehlektronnyeudarnye.html', locals())


def instrumentysmembranoj(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_instrumentysmembranoj = products_images.filter(product__category__id=5)
    return render(request, 'landing/instrumentysmembranoj.html', locals())


def samozvuchashchieinstrumenty(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_samozvuchashchieinstrumenty = products_images.filter(product__category__id=6)
    return render(request, 'landing/samozvuchashchieinstrumenty.html', locals())


def zapchastiikomplektuyushchie(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_zapchastiikomplektuyushchie = products_images.filter(product__category__id=9)
    return render(request, 'landing/zapchastiikomplektuyushchie.html', locals())


def barabannyepalochkiishchyotki(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_barabannyepalochkiishchyotki = products_images.filter(product__category__id=10)
    return render(request, 'landing/barabannyepalochkiishchyotki.html', locals())


def checkout_order(request):
    return render(request, 'orders/checkout-order.html', locals())