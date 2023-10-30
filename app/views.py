from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.
def greeting(request: HttpRequest, name:str) -> HttpResponse:
    names = (str(name))
    return HttpResponse(f"Hello, {names}")
def how_old(request: HttpRequest,end:int,birthyear:int) -> HttpResponse:
    age=(end-birthyear)
    return HttpResponse(age)
def order(request: HttpRequest, burgers:int, fries:int, drinks:int) -> HttpResponse:
    burger_price = 4.50
    fries_price = 1.5
    drinks_price = 1
    burger_total = burgers * burger_price
    fries_total = fries * fries_price
    drinks_total = drinks * drinks_price
    total = burger_total + fries_total + drinks_total
    return HttpResponse(total)
