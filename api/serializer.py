from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pizza
        fields=[ '_id', 'pizzaType', 'pizzaSize','pizzaTopping']