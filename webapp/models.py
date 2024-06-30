from django.db import models

# Create your models here.

class Records(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    
    
    def __str__(self) :
        firstname = self.first_name
        lastname = self.last_name
        return  f"{firstname} {lastname}"
       