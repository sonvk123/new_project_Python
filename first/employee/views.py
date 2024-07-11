import json
from django import forms
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

list_name = [
    {"name": "Son0", "age": 12},
    {"name": "Son1", "age": 13},
    {"name": "Son2", "age": 14},
    {"name": "Son3", "age": 15},
]

product = [
    {"name": "Áo thun", "price": 15.99},
    {"name": "Quần jean", "price": 29.99},
    {"name": "Giày thể thao", "price": 39.99},
    {"name": "Mũ", "price": 15.99},
]


def index(request):
    return HttpResponse("hi chào cậu")


def all(request):
    under = int(request.GET.get("under", 0))
    result = list_name
    if under:
        result = [e for e in list_name if (e["age"] < under)]
    return HttpResponse([f"<p>{e["name"]}</p>" for e in result])


def hello(request, name):
    return HttpResponse(f"<h1>Hello: {name.upper()} </h1>")


class NewEmployeesForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=18, max_value=60)


class NewProductForm(forms.Form):
    price = forms.IntegerField()


@csrf_exempt
def add(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            form = NewEmployeesForm(data)
            if form.is_valid():
                list_name.append(data)
                response_data = (
                    {"success": True, " message": "data saved !!!"})
            else:
                response_data = ({"success": False, " message": form.errors})
        except json.JSONDecodeError:
            response_data = (
                {"success": False, " message": "Invalid json data"})
        return JsonResponse(response_data)
    else:
        return JsonResponse({"success": False, " message": "Invalid json data"})

product = [
    {"name": "Áo thun", "price": 15.99},
    {"name": "Quần jean", "price": 29.99},
    {"name": "Giày thể thao", "price": 39.99},
    {"name": "Mũ", "price": 15.99},
]

def getProduct(request):
    index = request.GET.get("index")
    length = len(product)
    if index:
        index = int(index)
        if 0 <= index < length:
            selected_product = product[index]
            return HttpResponse(json.dumps(selected_product))
        else:
            return HttpResponse("Không tìm thấy sản phẩm cần tìm")
    else :
      return HttpResponse([f"<p>{e["name"], e["price"]}</p>" for e in product])


@csrf_exempt
def postProduct(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            form = NewProductForm(data)
            if form.is_valid():
                product.append(data)
                response_data = (
                    {"success": True, " message": "data saved !!!"})
            else:
                response_data = ({"success": False, " message": form.errors})
        except json.JSONDecodeError:
            response_data = (
                {"success": False, " message": "Invalid json data"})
        return JsonResponse(response_data)
    else:
        return JsonResponse({"success": False, " message": "Invalid json data"})


# def getProductIndex(request):
#     index = int(request.GET.get("index", 0))
#     length = len(product)
#     if index:
#         if 0 <= index < length:
#             return HttpResponse(product[index])
#         else:
#             return HttpResponse("Không tìm thấy sản phẩm cần tìm")
#     else :
#       return HttpResponse("Không tìm thấy index")
#     # result = product
#     # if index:
#     #     result = [e for e in list_name if (e["age"] < index)]
#     # return HttpResponse([f"<p>{e["name"]}</p>" for e in result])
