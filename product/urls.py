from django.urls import path
from .views import home,newItem,addItem,showItem,itemDetails

urlpatterns = [
    path('newitem/', newItem),
    path('home/', home),
    path('additem/', addItem),
    path('showitems/', showItem),
    path('itemDetails/<str:itemBrand>', itemDetails),
]