from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Category(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='Category/', default='Category/default.jpg')

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=0, max_digits=12)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    picture = models.ImageField(upload_to='products/', blank=True, null=True)
    star = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=0, max_digits=12)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=400, default='', blank=True)
    phone = models.CharField(max_length=20, blank=True)
    data = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
