
from django.urls import path
from .views import *
urlpatterns = [
    path('get/', get_pizzaDetail, name='getPizzaDetail'),
    path('update/<id>', update_pizzaDetail, name='updatePizzaDetail'),
    path('delete/<id>', delete_pizzaDetail, name='deletePizzaDetail'),
    path('post', post_pizzaDetail, name='postPizzaDetail'),
]