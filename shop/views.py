from django.shortcuts import render, redirect
from .forms import product
from .models import item

# Create your views here.
def add(request):
    if request.method =='GET':
        form = product()
    else:
        form = product(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')
    return render(request,'add.html',{'form':form})

def list(request):
    items= item.objects.all()
    return render(request,'list.html',{'items':items})

def edit(request, id):
    if request.method =='GET':
        if id!=0:
            items = item.objects.get(pk=id)
            form =(product(instance=items))
        return render(request,'add.html',{'form':form})
    else:
        if id!=0:
            items = item.objects.get(pk=id)
            form = product(request.POST, instance=items)
        if form.is_valid():
            form.save()
        return redirect('list')
    return render(request,'add.html',{'form':form})

def delt(request, id):
    items = item.objects.get(pk=id)
    items.delete()
    return redirect('list')