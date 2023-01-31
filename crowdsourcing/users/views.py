from django.shortcuts import render
from markets.models import Items, Categories, Markets
# Create your views here.


def index(request):
    return render(request, 'users/index.html', {"showtable": False})


def searchitem(request):
    item_name = request.POST.get('itemname')
    district = request.POST.get('district')
    area = request.POST.get('area')
    message = ""

    items = Items.objects.filter(item_name=item_name).order_by("price")
    results = []

    if not district and not area:
        if items:
            for i in items:
                c = Categories.objects.filter(pk=i.category_id)
                m = Markets.objects.filter(id=c[0].market_id)

                results.append({
                    "item_id": i.id,
                    "item_name": i.item_name,
                    "price": i.price,
                    "market_name": m[0].market_name,
                    "district": m[0].district,
                    "area": m[0].area,
                    "updated_at": i.updated_at
                })
        else:
            message = "Item currently unavailable!"

    elif not area:
        if items:
            for i in items:
                c = Categories.objects.filter(pk=i.category_id)
                m = Markets.objects.filter(
                    district=district, id=c[0].market_id)
                if m:
                    results.append({
                        "item_id": i.id,
                        "item_name": i.item_name,
                        "price": i.price,
                        "market_name": m[0].market_name,
                        "district": m[0].district,
                        "area": m[0].area,
                        "updated_at": i.updated_at
                    })
                else:
                    message = f"Item unavailable in {district}. Try searching without district!"
        else:
            message = "Item currently unavailable!"

    else:
        if items:
            for i in items:
                c = Categories.objects.filter(pk=i.category_id)
                m = Markets.objects.filter(
                    district=district, area=area, id=c[0].market_id)
                if m:
                    results.append({
                        "item_id": i.id,
                        "item_name": i.item_name,
                        "price": i.price,
                        "market_name": m[0].market_name,
                        "district": m[0].district,
                        "area": m[0].area,
                        "updated_at": i.updated_at
                    })
                else:
                    message = f"Item unavailable in {area}, {district}. Try searching without area & district!"
        else:
            message = "Item currently unavailable!"

    return render(request, 'users/index.html', {"results": results, "showtable": True, "message": message})
