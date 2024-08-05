from django.db import models

# Create your models here.
allProducts = (('burger', 'Burger'), ('pizza', 'Pizza'), ('biryani', 'Biryani'), ('noodles', 'Noodles'), ('cake', 'Cake'), ('momos', 'Momos'),
               ('ice cream', 'Ice cream'), ('shakes', 'Shakes'), ('northfood', 'Northfood'), ('southfood', 'Southfood'), ('offer', 'Offer'), ('topfood', 'Topfood'))


class products(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField((""), upload_to=None, )
    category = models.CharField(choices=allProducts, max_length=255)
    info = models.TextField()


class Users(models.Model):
    name = models.CharField(max_length=255)
    pwd = models.CharField(max_length=255)
    address = models.TextField()
    email =models.EmailField()
    phone = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    cart = models.JSONField()
    # {products:[]}