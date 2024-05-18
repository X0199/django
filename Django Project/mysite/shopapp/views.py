from django.http import HttpResponse
from django.shortcuts import render
from timeit import default_timer

def shop_index(request):
    # print(request.path)
    # print(request.method)
    products = [
        ("Laptop", 999),
        ("Desktop", 1999),
        ("Smartphone", 2999),
    ]
    context = {
        "Time_running": default_timer(),
        "products": products
    }

    return render(request,"shopapp/index.html", context=context)