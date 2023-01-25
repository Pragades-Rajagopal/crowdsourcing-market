from django.shortcuts import render, get_object_or_404, redirect
from .models import Markets, Categories, Items
from datetime import datetime
from django.utils import timezone

# Create your views here.


def index(request):
    markets = Markets.objects.all()
    return render(request, 'markets/index.html', {"markets": markets})


def categories(request, market_id):
    categories = Categories.objects.filter(market_id=market_id)
    return render(request, 'markets/categories.html', {"categories": categories})


def items(request, category_id):
    items = Items.objects.filter(category_id=category_id).order_by('price')
    return render(request, 'markets/items.html', {"items": items, "category_id": category_id})


def get_addItems(request, category_id):
    return render(request, 'markets/add-items.html', {"category_id": category_id})


def postitem(request):
    item_name = request.POST.get('itemname')
    price = request.POST.get('price')
    updated_by = request.POST.get('user')
    category_id = request.POST.get('category_id')
    updated_at = datetime.now()
    inputs = Items(item_name=item_name, price=price, updated_at=updated_at,
                   updated_by=updated_by, category_id=category_id)
    inputs.save()

    items = Items.objects.filter(category_id=category_id).order_by('price')
    return render(request, 'markets/items.html', {"items": items, "category_id": category_id})


def getItem(request, item_id):
    item = get_object_or_404(Items, pk=item_id)
    return render(request, 'markets/add-items.html', {"item": item, "if_get_item": True})


def updateItem(request, item_id):
    item_name = request.POST.get('itemname')
    price = request.POST.get('price')
    updated_by = request.POST.get('user')
    category_id = request.POST.get('category_id')
    updated_at = datetime.now()
    update = Items.objects.get(pk=item_id)
    update.item_name = item_name
    update.price = price
    update.updated_at = updated_at
    update.updated_by = updated_by
    update.category_id = category_id
    update.save()

    items = Items.objects.filter(category_id=category_id).order_by('price')
    return render(request, 'markets/items.html', {"items": items, "category_id": category_id})
