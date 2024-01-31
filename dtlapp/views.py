from django.shortcuts import render
from datetime import datetime

# Create your views here.
# def index(req):
#     username = (input("Enter Username = "))
#     context = {"username" : username}
#     # return render(req, "index.html", {"username": username})
#     return render(req, "index.html", context)

def index(req):
    username = "admin"
    products = ["mobile", "laptop", "pc", "keyboard"]
    movies = {"kgf": 5, "jawan": 4, "leo": 3}
    fruitsdata = fruits()
    context = {"username" : username, "products": products, "movies":movies, "fruitsdata" : fruitsdata}
    return render(req, "index.html", context)  

def fruits():
    fruitlist = ("graps", "mango", "apple")
    return fruitlist

def login(req):
    username = input("enter username = ")
    todaysdate = datetime.now()
    context = {"username": username, "todaysdate": todaysdate}
    return render(req, "login.html", context)