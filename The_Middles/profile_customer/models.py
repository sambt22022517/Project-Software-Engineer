from django.db import models

# Create your models here.
class Order(models.Model):
    ID_Order = models.CharField()
    ID_Customer = models.CharField()
    Status = models.CharField(choices=[('WP', 'Wait for pay'),('D','Delivery'),
                                       ('WD','Wait for delivery'),('CP','Complete'),
                                       ('C','Canceled'),('R', 'Reimbustment')])
    ID_Product = models.CharField()
    Time = models.DateTimeField()
    Quantity = models.IntegerField(default=1)
    Unit_price = models.FloatField()

class Product(models.Model):
    ID_Product = models.CharField()
    Description = models.TextField()
    ID_shop = models.CharField()

class Customer(models.Model):
    ID_Customer = models.CharField()
    Name = models.CharField(max_length=255)
    Phone_number = models.IntegerField(max_length = 20)
    Andress = models.TextField()


        
