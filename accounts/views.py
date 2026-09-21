from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .models import Task, User
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def todo(request):
    if request.method == 'POST':
        task_1 = request.POST.get("task_input")
        if task_1:
            Task.objects.create(name=task_1, author=request.user) #тут можно написать (author_id=request.user.id), но джанго модели позволяют и такое.
    tasks = Task.objects.filter(author=request.user)

    return render(request, "tasks.html", {"tasks": tasks})

def enter(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            account = form.get_user()
            login(request, account)
            return redirect('todo')
    
    else:
        form = AuthenticationForm()

    return render(request, "enter.html", {"form": form})

def exit(request):
    if request.method == 'POST':
        logout(request)
        return redirect("enter")

def create_account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            account = form.save()
            login(request, account)
            return redirect('todo')

    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})

def edit(request, task_id):
    old = Task.objects.get(id=task_id, author=request.user)
    if request.method == 'POST':
        task_edit = request.POST.get("task_edit")
        if task_edit:
            old.name = task_edit
            old.save()
            return redirect("todo")
    return render(request, "edit.html", {"task_name": old.name}) 

def delete(request, task_id):
    if request.method == 'POST':
        task_del = Task.objects.get(id=task_id, author=request.user)
        task_del.delete()
        return redirect("todo")
    return redirect("todo")


