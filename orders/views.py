from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *
from django.contrib.auth.decorators import login_required
from pprint import pprint
cart =0
d={'Antipasto_l': 75.0,
 'Baked_Ziti_l': 65.0,
 'Baked_Ziti_w_Chicken_l': 9.75,
 'Baked_Ziti_w_Meatbal_l': 8.75,
 'Baked_Ziti_w_Mozzare_l': 6.5,
 'Cheese_l': 7.95,
 'Cheese_s': 6.5,
 'Chicken_Parm_l': 85.0,
 'Chicken_Parmigiana_l': 8.5,
 'Chicken_Parmigiana_s': 7.5,
 'Eggplant_Parmigiana_l': 7.95,
 'Eggplant_Parmigiana_s': 6.5,
 'Garden_Salad_l': 65.0,
 'Greek_Salad_l': 75.0,
 'Ham_+_Cheese_l': 7.95,
 'Ham_+_Cheese_s': 6.5,
 'Italian_l': 7.95,
 'Italian_s': 6.5,
 'Meatball_Parm_l': 75.0,
 'Meatball_l': 7.95,
 'Meatball_s': 6.5,
 'Salad_w_Tuna_l': 8.25,
 'Steak_+_Cheese_l': 8.5,
 'Steak_+_Cheese_s': 6.95,
 'Steak_l': 7.95,
 'Steak_s': 6.5,
 'Tuna_l': 7.95,
 'Tuna_s': 6.5,
 'Turkey_l': 8.5,
 'Turkey_s': 7.5,
 'pizza1_topping_l': 13.71,
 'pizza1_topping_s': 19.95,
 'pizza2_toppings_l': 15.21,
 'pizza2_toppings_s': 21.95,
 'pizzaCheese_l': 17.95,
 'pizzaCheese_s': 12.71,
 'spizza1_item_l': 26.45,
 'spizza1_item_s': 40.7,
 'spizzaCheese_l': 24.45,
 'spizzaCheese_s': 38.7}
def home(request):
    return render(request,"orders/home.html")


def menu(request):
    return render(request,'orders/menu.html',
    {'p':Pizzas.objects,
    's':SicPizzas.objects,'cart':cart,
    'sub':Subs.objects,
    'pasta':Pasta.objects,
    'salad':Salads.objects,
    'dinner':Dinner.objects,
    'toppings':Toppings.objects,
    })




@login_required(login_url='/loginUser')
def viewCart(request):
    pt = 0
    qt=0
    if request.method == 'POST':
        data =  request.POST['data']
        x=data.split(",")
        cart_items={}
        for a in x:
            cart_items[a]={'quantity':x.count(a),'price':d[a]*x.count(a)}
            pt+=float(d[a])
        if "" in cart_items.keys():
            return render(request,'orders/viewCart.html',{"msg":"your cart is empty"})

        for x in cart_items.keys():
            qt+=cart_items[a]['quantity']
        pt=round(pt,2)
    return render(request,'orders/viewCart.html',{"items":cart_items,"pt":pt,'qt':qt,'cartcount':request.POST['cartcount']})


def placeOrder(request):
    if request.method == 'POST':
        orders_list = request.POST['olist']
        cname = request.POST['customer_name']
        print()
        print(orders_list)
        print(cname)
        print()
        print()
        
        #return render(request,'orders/home.html',{'gmsg':'order placed'})
        return HttpResponse("order placed")



def dataTester(request):
    global d
    for a in Pizzas.objects.all():
        d[a.idSmall()]=a.ps
        d[a.idLarge()]=a.pl

    for a in SicPizzas.objects.all():
        d[a.idSmall()]=a.ps
        d[a.idLarge()]=a.pl

    for a in Subs.objects.all():
        d[a.idSmall()]=a.ps
        d[a.idLarge()]=a.pl

    for a in Pasta.objects.all():
        d[a.idLarge()]=a.pl

    for a in Salads.objects.all():
        d[a.idLarge()]=a.pl

    for a in Dinner.objects.all():
        d[a.idLarge()]=a.pl

    pprint(d)
    return HttpResponse(d.items())



def loginUser(request):
    if User.is_authenticated:
        print()
        print("authenticate")
        if User.is_anonymous:
            auth.logout(request)
        else:
            return redirect('home')
    if request.method =='POST':
        user=auth.authenticate(username=request.POST['u'],password=request.POST['p'])
        if user:
            auth.login(request,user)
            return render(request,'orders/home.html')
        else:
            return render(request,'orders/login.html',{'msg':'wrong creds'})
    return render(request,'orders/login.html')

def signupUser(request):
    if User.is_authenticated:

        if User.is_anonymous:
            auth.logout(request)
        else:
            return redirect('home')
    if request.method =='POST':
        if request.POST['p1']==request.POST['p2']:
            try:
                u=User.objects.get(username=request.POST['u'])
                return render(request,'orders/signup.html', {'msg':'username alerady taken'} )
            except User.DoesNotExist:
                user= User.objects.create_user(request.POST['u'],password=request.POST['p1'])
                auth.login(request,user)
                return redirect('home')
        else:
                return render(request,'orders/signup.html', {'msg':'passwords must match'} )

    return render(request,'orders/signup.html')


def logoutUser(request):
    if request.method == 'POST':
        auth.logout(request)
    return render(request,'orders/home.html',{'msg':"peaceoutnibba"})
