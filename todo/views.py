from django.shortcuts import render, redirect
from path.models import *

def index(request):
    if request.user.is_authenticated:
        items = Item.objects.filter(user=request.user)
        return render(request, 'todo/home.html', {
            'items': items
        })
    else:
        return render(request, 'todo/index.html')

def new_item(request):
    if request.method == 'GET':
        return render(request, 'todo/new-item.html')
    elif request.method == 'POST':
        name = request.POST['name']
        user = request.user
        Item(name=name, user=user).save()
        return redirect('/')
    
def delete_item(request, item):
    Item.objects.filter(pk=item)[0].delete()
    return redirect('/')