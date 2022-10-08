from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo

def Home(request):
    if request.method =="POST":
        title = request.POST.get('title')
        if title !="":
            Todo.objects.create(title=title)
        return redirect('home')
    data=Todo.objects.all()
    data_dict={"data":data}
    return render(request,'home.html',context=data_dict)

def Delete(request,id=None):
    Todo.objects.get(id=id).delete()
    return redirect('home')

def Complete(request,id=None):
    data = Todo.objects.get(id=id)
    data.complete=True
    data.save()
    return redirect('home')

def InComplete(request,id=None):
    data = Todo.objects.get(id=id)
    data.complete =False
    data.save()
    return redirect('home')
