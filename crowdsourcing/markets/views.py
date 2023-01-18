from django.shortcuts import render
from .models import Markets, Categories, Items

# Create your views here.


def index(request):
    markets = Markets.objects.all()
    return render(request, 'markets/index.html', {"markets": markets})
