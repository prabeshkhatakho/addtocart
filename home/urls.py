
from django.urls import path
from .views import *
app_name = "home"

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('subcategory/<slug>', SubCategoryView.as_view(), name = 'home'),
    path('details/<slug>', DetailView.as_view(), name = 'home'),
    path('search', SearchView.as_view(), name = 'search'),
    path('signup',signup, name = 'signup'),
    path('cart/<id>',cart, name = 'cart')
]