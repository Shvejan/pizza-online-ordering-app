from .models import *
d = {}
for a in Pizzas.objects:
    d['a.idSmall()']=a.ps
    d['a.idLarge()']=a.pl

print(d)
