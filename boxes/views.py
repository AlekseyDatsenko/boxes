from django.shortcuts import render
from .models import About, Contact, Stock, Delivery, Box_1, Box_2, Box_3
    
def about(request):
    about = About.objects.all()
    contact = Contact.objects.all()
    return render(request, 'boxes/about.html', {'about':about, 'contact':contact,})

def contacts(request):
    contacts = Contact.objects.all()
    contact = Contact.objects.all()
    return render(request, 'boxes/contacts.html', {'contacts':contacts, 'contact':contact,})

def stock(request):
    stock = Stock.objects.all()
    contact = Contact.objects.all()
    return render(request, 'boxes/stock.html', {'stock':stock, 'contact':contact,})

def delivery(request):
    delivery = Delivery.objects.all()
    contact = Contact.objects.all()
    return render(request, 'boxes/delivery.html', {'delivery':delivery, 'contact':contact,})

def boxes(request):
    boxes_1 = Box_1.objects.all()
    boxes_2 = Box_2.objects.all()
    boxes_3 = Box_3.objects.all()
    contact = Contact.objects.all()
    return render(request, 'boxes/boxes.html', {'boxes_1':boxes_1, 'boxes_2':boxes_2, 'boxes_3':boxes_3, 'contact':contact,})
