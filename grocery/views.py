from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import  HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import User, GroceryItem


def index(request):
    if request.user.is_authenticated:
        currentUser = User.objects.filter(username=request.user.username)[0]
        userItems = GroceryItem.objects.filter(user=currentUser).all().order_by('-date')
        context = {
            "userItems": userItems
        }
        return render(request, "grocery/index.html", context=context)
    return render(request, "grocery/index.html")

def addListView(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            currentUser = User.objects.filter(username=request.user.username)[0]
            itemName = request.POST.get('item-name')
            itemQuantity = request.POST.get('item-quantity')
            itemStatus = request.POST.get('item-status')
            itemDate = request.POST.get('item-date')
            GroceryItem.objects.create(
                user = currentUser, 
                name = itemName,
                amount = itemQuantity,
                status = itemStatus,
                date = itemDate
            )
            return HttpResponseRedirect(reverse('index'))
        return render(request, "grocery/index.html")

    if request.user.is_authenticated:
        context = {}
        return render(request, "grocery/add.html", context=context)
    return render(request, "grocery/add.html")

def edit(request, itemId):
    if request.method == 'POST':
        try:
            item = GroceryItem.objects.filter(id=itemId)[0]
            context = {
                "itemId": itemId,
                "itemName": item.name,
                "itemAmount": item.amount,
                "itemStatus": item.status,
                "itemDate": "{0:0=2d}".format(item.date.year) + "-" + "{0:0=2d}".format(item.date.month) + "-" + "{0:0=2d}".format(item.date.day)
            }
            # print(context)
            return render(request, "grocery/update.html", context=context)
        except LookupError as e:
            data = {
                "response": e
            }
            return JsonResponse(data, status=400)
    try:
        item = GroceryItem.objects.filter(id=itemId)[0]
        item.name = request.GET.get('name')
        item.amount = request.GET.get('quantity')
        item.status = request.GET.get('status')
        item.date = request.GET.get('date')
        item.save()
        return HttpResponseRedirect(reverse('index'))
    except LookupError as e:
            data = {
                "response": e
            }
            return JsonResponse(data, status=400)

def delete(request, itemId):
    if request.method == "POST":
        try:
            item = GroceryItem.objects.filter(id=itemId)[0]
            item.delete()
            return HttpResponseRedirect(reverse('index'))
        except LookupError as e:
            data = {
                "response": e
            }
            return JsonResponse(data, status=400)
    data = {
        "response": "Method not allowed"
    }
    return JsonResponse(data, status=405)

def filter(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            currentUser = User.objects.filter(username=request.user.username)[0]
            userItems = GroceryItem.objects.filter(user=currentUser).all()
            filteredItems = userItems.filter(date=request.POST.get("filter-date")).all().order_by('-date')
            context = {
                "userItems": filteredItems,
                "date": request.POST.get("filter-date")
            }
            return render(request, "grocery/index.html", context=context)
        return render(request, "grocery/index.html")
    data = {
        "response": "Method not allowed"
    }
    return JsonResponse(data, status=405)

def loginView(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "grocery/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "grocery/login.html")


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "grocery/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "grocery/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "grocery/register.html")
