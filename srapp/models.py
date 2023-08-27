from django.db import models

# Create your models here.


class SalesData(models.Model):
    sno = models.CharField(max_length=100,default=0)
    Date = models.CharField(max_length=100,default=0)
    Costumer_Id = models.CharField(max_length=100,default=0)
    Costumer_Name = models.CharField(max_length=100,default="")
    email = models.EmailField(max_length=100)
    Alt_email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100,default=0)
    Alt_phone = models.CharField(max_length=100,default=0)
    Address = models.CharField(max_length=100,default="")
    Service = models.CharField(max_length=100,default="")
    Price = models.CharField(max_length=100,default=0)
