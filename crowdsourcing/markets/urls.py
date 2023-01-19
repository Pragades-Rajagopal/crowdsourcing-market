from django.urls import path
from . import views


app_name = 'markets'
urlpatterns = [
    path('', views.index, name='index'),
    path('categories/<int:market_id>', views.categories, name='categories'),
    path('items/<int:category_id>', views.items, name='items'),
    path('add-item/<int:category_id>', views.get_addItems, name='get_addItems'),
    path('postitem/', views.postitem, name='postitem')
]
