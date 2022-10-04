from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    _todos = Todo.objects.all().order_by("priority")
    context = {
        "todos": _todos,
    }
    return render(request, "todos/index.html", context)


def create(request):
    content = request.GET.get("formcontent")
    priority = request.GET.get("formpriority")
    deadline = request.GET.get("formdate")
    Todo.objects.create(content=content, priority=priority, deadline=deadline)
    return redirect("todos:index")


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("todos:index")


def complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("todos:index")
