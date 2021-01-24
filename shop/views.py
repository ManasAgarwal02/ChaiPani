from math import ceil
import json
from django.shortcuts import render, redirect
from .forms import *
import uuid


# Create your views here.

def index(request):
    allProds = []
    # getting the products categories and id
    category_of_products = Product.objects.values('category', 'id')
    # getting all the categories of food
    categories = {item['category'] for item in category_of_products}

    for category in categories:
        product = Product.objects.filter(category=category)
        n = len(product)
        nSlides = (n // 4) + ceil((n / 4) - (n // 4))
        allProds.append([product, range(1, nSlides), nSlides])

    params = {'allProds': allProds}

    return render(request, 'index.html', params)


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search', "")
    allProds = []
    category_of_products = Product.objects.values('category', 'id')
    categories = {item['category'] for item in category_of_products}

    for category in categories:
        productTemp = Product.objects.filter(category=category)
        product = [item for item in productTemp if searchMatch(query, item)]
        n = len(product)
        nSlides = (n // 4) + ceil((n / 4) - (n // 4))
        if len(product) != 0:
            allProds.append([product, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'index.html', params)


def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
    else:
        form = OrderForm()
    return render(request, 'checkout.html', {'form': form})


def preview(request):
    params = {}
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        # form.save()
        item_json = request.POST.get('itemJson', '')
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        image = request.FILES.get('id_image', "")
        empId = request.POST.get('emp_id', "")
        org = request.POST.get('organisation', "")
        item_json = json.loads(item_json)
        myOrder = Order(name=name, email=email, phone=phone, id_image=image, emp_id=empId, organisation=org,
                        items_json=item_json)
        myOrder.save()
        params = {
            'item_json': item_json,
            'name': name,
            'email': email,
            'phone': phone,
            'image': image,
            'empId': empId,
            'org': org
        }
    return render(request, 'preview.html', params)


def confirm(request):
    params = {'id': str(uuid.uuid4())[:8]}
    return render(request, 'confirm.html', params)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
