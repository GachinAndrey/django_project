from django.db import models
from mainapp.models import Product
from django.contrib.auth import get_user_model

class BasketManager(models.Manager):
    def quantity(self):
        return sum([item.quantity for item in self.all()])
    
    def basket_sum(self):
        return sum([item.product.price * item.quantity for item in self.all()])

class Basket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='basket')
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = BasketManager()

def __str__(self):
    return f'{self.product} - {self.quantity} шт'