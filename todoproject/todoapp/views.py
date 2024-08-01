# todoapp/views.py
from django.shortcuts import render,get_object_or_404, redirect
from .models import Tasks
from .models import TodoItem
from .forms import TodoForm




def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todoapp/todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todoapp/todo_form.html', {'form': form})

def todo_update(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todoapp/todo_form.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todoapp/todo_confirm_delete.html', {'todo': todo})

def todo_done(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    todo.done = True
    todo.save()
    return redirect('todo_list')

def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'todoapp/task_list.html', {'tasks': tasks})


