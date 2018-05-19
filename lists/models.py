from django.db import models


# Create your models here.
class List(models.Model):
    pass


# class Beef(models.Model):
#     pass
#    type = models.TextField(default='')
#    amount = models.TextField(default='')
#    price = models.TextField(default = '')
#    username = models.TextField(default = '')

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)




