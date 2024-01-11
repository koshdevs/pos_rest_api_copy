from django.db import models

# Create your models here.

class Stocks(models.Model):

    serial = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    qty = models.FloatField(default=0.0)
    cost = models.FloatField(default=0.0)
    date = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=20)
    shop_id = models.CharField(max_length=20)
    remarks = models.TextField(default="")

    def __str__(self):

        return str(self.name)
    
    class Meta:

        verbose_name = "Stocks"
        verbose_name_plural = "Stocks"
    

    