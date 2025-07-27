from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from apps.todo.models import TodoList
from apps.todo.forms import TodoForm

ALL_CHECKED: bool = False

@login_required
def todolist(request):
    if request.method == "POST":
        form = TodoForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
        # messages.success(request,("New task added successfully!"))
        return redirect('todolist')
    todos = TodoList.objects.filter(manage=request.user)
    paginator = Paginator(todos, 5)
    page = request.GET.get('pg')
    todos = paginator.get_page(page)
    return render(request, 'todo/todos.html', context={'todos': todos})

@login_required
def delete_task(request, task_id):
    task = TodoList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
        # messages.success(request,("Task deleted successfully!"))
    else:
       messages.error(request,("Access Restricted"))
    return redirect('todolist')

@login_required
def delete_tasks(request):
    todos = TodoList.objects.filter(manage=request.user)
    todos.delete()
    # messages.success(request,("Tasks deleted successfully!"))
    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = TodoList.objects.get(pk=task_id)
        form = TodoForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        # messages.success(request,("Task edited successfully!"))
        return redirect('todolist')
    todo = TodoList.objects.get(pk=task_id)
    return render(request, 'todo/edit.html', {'todo': todo})

@login_required
def complete_task(request, task_id):
    task = TodoList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.is_done = True
        task.save()
        # messages.success(request,("Marked task as 'Completed' successfully!"))
    else:
        messages.error(request,("Access Restricted")) 
    return redirect('todolist')

@login_required
def complete_tasks(request):
    global ALL_CHECKED
    tasks = TodoList.objects.filter(manage=request.user)
    for task in tasks:
        task.is_done = True if not ALL_CHECKED else False
        task.save()
        # messages.success(request,("Marked all tasks as 'Completed' successfully!"))
    ALL_CHECKED = not ALL_CHECKED
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    global ALL_CHECKED
    ALL_CHECKED = False
    task = TodoList.objects.get(pk=task_id)
    task.is_done = False
    task.save()
    # messages.success(request,("Marked task as 'Pending' successfully!"))
    return redirect('todolist')
