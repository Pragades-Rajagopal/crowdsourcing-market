from django.shortcuts import render
from markets.models import Items, Categories, Markets
# Create your views here.


def index(request):
    return render(request, 'users/index.html')


def searchitem(request):
    item_name = request.POST.get('itemname')
    district = request.POST.get('district')
    area = request.POST.get('area')

    items = Items.objects.filter(item_name=item_name).order_by("price")
    result = []
    # for i in items:
    #     c = Categories.objects.filter(pk=i.category_id)
    #     m = Markets.objects.filter(id=c[0].market_id)
    #     print(m[])
    #     result.append(
    #         {"market_name": m[0].market_name, "item": items[i]})
    # print(result)
    return render(request, 'users/searchitems.html', {"items": items})
