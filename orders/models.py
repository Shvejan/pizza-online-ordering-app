from django.db import models
from django_mysql.models import ListCharField
# Create your models here.
class Pizzas(models.Model):
    name = models.CharField(max_length = 20)
    img = models.ImageField(upload_to='images/')
    pl = models.FloatField()
    ps = models.FloatField()
    top = models.IntegerField()

    def idSmall(self):
        return 'pizza'+self.name.replace(" ","_").replace("/","_") +"_s"
    def idLarge(self):
        return 'pizza' + self.name.replace(" ","_").replace("/","_") +"_l"

    def __str__(self):
        return self.name

class SicPizzas(models.Model):
    name = models.CharField(max_length = 20)
    img = models.ImageField(upload_to='images/')
    pl = models.FloatField()
    ps = models.FloatField()
    top = models.IntegerField()


    def __str__(self):
        return self.name

    def idSmall(self):
        return 'spizza' + self.name.replace(" ","_").replace("/","_") +"_s"
    def idLarge(self):
        return 'spizza' +self.name.replace(" ","_").replace("/","_") +"_l"



class Subs(models.Model):
    img=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=20)
    pl = models.FloatField()
    ps = models.FloatField()

    def __str__(self):
        return self.name
    def idSmall(self):
        return self.name.replace(" ","_").replace("/","_") +"_s"
    def idLarge(self):
        return self.name.replace(" ","_").replace("/","_") +"_l"

class Pasta(models.Model):
    img=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=20)
    pl = models.FloatField()

    def __str__(self):
        return self.name
    def idLarge(self):
        return self.name.replace(" ","_").replace("/","_") +"_l"

class Salads(models.Model):
    img=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=20)
    pl = models.FloatField()

    def idLarge(self):
        return self.name.replace(" ","_").replace("/","_") +"_l"
    def __str__(self):
        return self.name


class Toppings(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Dinner(models.Model):
    name = models.CharField(max_length = 20)
    img = models.ImageField(upload_to='images/')
    pl = models.FloatField()
    ps = models.FloatField()

    def idSmall(self):
        return self.name.replace(" ","_").replace("/","_") +"_s"
    def idLarge(self):
        return self.name.replace(" ","_").replace("/","_") +"_l"

    def __str__(self):
        return self.name

class Orders(models.Model):
    customer_name = models.CharField(max_length=20)
    order_items =   ListCharField()
