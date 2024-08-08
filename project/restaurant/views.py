import json
from ast import literal_eval
from django.shortcuts import render, redirect
from .models import products, Users

# Create your views here.
isLoggedIn = False

userId: int = 3

def remove_duplicates(lst):
    seen = {}
    result = []
    
    for sublist in lst:
        key = sublist[0]
        if key not in seen:
            seen[key] = True
            result.append(sublist)
    
    return result

def homepage(req):
    user = req.session.get('userID')
    if not user:
        return redirect('/login')
    else:
        db = products.objects.filter(category="topfood").values()
        clearDb = list(db)
        for i in clearDb:
            i.update({'image': i['image'].replace('None/', '')})
            i.update({'image': i['image'].split('_')[
                0]+i['image'].split('_')[1][-4:]})

        db1 = products.objects.filter(category="offer").values()
        clearDb1 = list(db1)
        print(clearDb)
        for i in clearDb1:
            i.update({'image': i['image'].replace('None/', '')})
        return render(req, 'index.html', context={"topfood": clearDb, "offers": clearDb1})


def burgerpage(req):
    db = products.objects.filter(category="burger").values()
    clearDb = list(db)
    for i in clearDb:
        print(i['image'])
        i.update({'image': i['image'].replace('None/', '')})
    return render(req, 'burger.html', context={"data": clearDb})


def biryanipage(req):
    db = products.objects.filter(category="biryani").values()
    clearDb = list(db)
    for i in clearDb:
        i.update({'image': i['image'].replace('None/', '')})
    return render(req, 'biryani.html', context={"data": clearDb})


def cakepage(req):
    db = products.objects.filter(category="cake").values()
    clearDb = list(db)
    for i in clearDb:
        i.update({'image': i['image'].replace('None/', '')})
    return render(req, 'cake.html', context={"data": clearDb})


def drinkpage(req):
    db = products.objects.filter(category="shakes").values()
    clearDb = list(db)
    for i in clearDb:
        i.update({'image': i['image'].replace('None/', '')})
    return render(req, 'drink.html', context={"data": clearDb})


def icecreampage(req):
    db = products.objects.filter(category="ice cream").values()
    clearDb = list(db)
    for i in clearDb:
        i.update({'image': i['image'].replace('None/', '')})
    return render(req, 'icecream.html', context={"data": clearDb})


def momospage(req):
    db = products.objects.filter(category="momos").values()
    clearDb = list(db)
    for i in clearDb:
        i.update({'image': i['image'].replace('None/', '')})
    return render(req, 'momos.html', context={"data": clearDb})


def noodlespage(req):
    db = products.objects.filter(category="noodles").values()
    clearDb = list(db)
    for i in clearDb:
        i.update({'image': i['image'].replace('None/', '')})
    return render(req, 'noodles.html', context={"data": clearDb})


def pizzapage(req):
    db = products.objects.filter(category="pizza").values()
    clearDb = list(db)
    for i in clearDb:
        i.update({'image': i['image'].replace('None/', '')})
    return render(req, 'pizza.html', context={"data": clearDb})


def northfoodpage(req):
    db = products.objects.filter(category="northfood").values()
    clearDb = list(db)
    for i in clearDb:
        i.update({'image': i['image'].replace('None/', '')})
    return render(req, 'northfood.html', context={"data": clearDb})


def southfoodpage(req):
    db = products.objects.filter(category="southfood").values()
    clearDb = list(db)
    for i in clearDb:
        i.update({'image': i['image'].replace('None/', '')})
    return render(req, 'southfood.html', context={"data": clearDb})


def productpage(req, Id):

    db = products.objects.filter(id=Id).values()
    clearDb = list(db)
    # print(clearDb)
    for i in clearDb:
        i.update({'image': i['image'].replace('None/', '')})
    return render(req, 'product.html', context={"data": clearDb})


def productpagess(req, Id):
    db = products.objects.filter(id=Id).values()
    clearDb = list(db)
    print(clearDb)
    for i in clearDb:
        i.update({'image': i['image'].replace('None/', '')})

    return render(req, 'productss.html', context={"data": clearDb})


def loginpage(req):
    if (req.method == "POST"):
        global userId
        phones = req.POST['phone']
        pwd = req.POST['password1']
        print(phones, pwd)
        user = Users.objects.get(phone=phones, pwd=pwd)
        print(user)

        if (user):
            userId = user.id
            req.session['userID'] = user.id
            print(userId)
            return redirect('/')

    return render(req, 'login.html')


def signuppage(req):
    if (req.method == 'POST'):
        uname = req.POST['name']
        passw = req.POST['password']
        emails = req.POST['email']
        phone = req.POST['phone']
        states = req.POST['state']
        citys = req.POST['city']
        addr = req.POST['address']
        Users.objects.create(name=uname, pwd=passw, email=emails,
                             phone=phone, state=states, city=citys, address=addr, cart={})
        return redirect('/')
    return render(req, 'signup.html')


def cartpage(req):
    Cartarray = []

    user = Users.objects.get(id=userId)
    for i in user.cart['products']:
        d = [products.objects.get(id=i[0]),i[1]]
        Cartarray.append(d)

    return render(req, 'cart.html', context={"data": Cartarray})


def addToCart(req, ID):
    params = req.GET.get('qty')
    print(params)
    global userId
    user = Users.objects.get(id=userId)
    user.cart['products'].append([ID, params])
    user.cart['products'] = remove_duplicates(user.cart['products'])
    # print("hello", user.cart['products'])
    user.save()
    return redirect('/product/'+str(ID)+'?added=true')


def addToCarts(req, ID):
    params = req.GET.get('qty')
    print(params)
    global userId
    user = Users.objects.get(id=userId)
    user.cart['products'].append((ID, params))
    user.cart['products'] = remove_duplicates(user.cart['products'])
    # print("hello", user.cart['products'])
    user.save()
    return redirect('/products/'+str(ID)+'?added=true')


def searchpage(req, item):
    db = products.objects.all().values()
    filterdb = []
    for i in db:
        if i['name'].lower().find(item) != -1:
            filterdb.append(i)
    return render(req, 'search.html', context={"data": filterdb})


def logout(req):
    req.session.clear()
    return redirect('/')


def aboutpage(req):
    return render(req, 'about.html')


def termpage(req):
    return render(req, 'term.html')


def privacypage(req):
    return render(req, 'privacy.html')


def helppage(req):
    return render(req, 'help.html')
