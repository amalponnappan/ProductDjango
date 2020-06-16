from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product
def home(req):
    template = loader.get_template('home.html')
    data = {}
    res = template.render(data,req)
    return HttpResponse(res)

def newItem(req):
    template = loader.get_template('additem.html')
    data = {}
    res = template.render(data,req)
    return HttpResponse(res)

def showItem(req):
    template = loader.get_template('showitems.html')
    val = Product.objects.all()
    print(val)
    data = {"itemlist":val}
    res = template.render(data,req)
    return HttpResponse(res)

def itemDetails(req,itemBrand):
    template = loader.get_template('itemDetails.html')
    val = Product.objects.get(brand = itemBrand)
    print(val)
    data = {"itemlist":[val]}
    res = template.render(data,req)
    return HttpResponse(res)

def addItem(req):
    # template = loader.get_template('additem.html')
    val = req.GET
    print(val)
    c = Product(brand = val['brand'],model = val['model'],price = int(val['price']))
    c.save()
    return HttpResponse('Item inserted')

# Create your views here.
