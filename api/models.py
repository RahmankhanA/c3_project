# from django.db import models
from django.db.models.enums import Choices
from djongo import models
# Create your models here.




class Pizza(models.Model):
    PIZZA_TYPES = (
        ('regular', 'Regular'),
        ('square', 'Square'),
        
    )
    PIZZA_SIZE =  (
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    )
    # _id=models.AutoField(primary_key=True)
    _id = models.ObjectIdField()
    pizzaType=models.CharField(max_length=50,choices=PIZZA_TYPES)
    
    pizzaSize=models.CharField( max_length=50, choices=PIZZA_SIZE)
    pizzaTopping=models.CharField( max_length=100)


    def __str__(self):
        return str(self._id)
    