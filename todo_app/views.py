from django.shortcuts import render, redirect

from todo_app.forms import todo_form

from todo_app.models import todo_db


def todo_list(request):
    todo = todo_db.objects.all()
    return render(request, 'todo_list.html', dict(todo=todo))


def todo_add(request):
    if request.method == 'POST':
        name = request.POST.get('todo', )
        level = request.POST.get('level', )
        created = request.POST.get('created', )
        todo_created = todo_db(name=name, level=level, created=created)
        todo_created.save()
        return redirect('todo_normal:todo_list')
    return render(request, 'todo_list.html')


def todo_delete(request, id):
    todo_remove = todo_db.objects.get(id=id)
    if request.method == 'POST':
        todo_remove.delete()
        return redirect('todo_normal:todo_list')
    return render(request, 'todo_delete.html', dict(task=todo_remove))


def todo_update(request, id):
    item = todo_db.objects.get(id=id)
    form = todo_form(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('todo_normal:todo_list')
    return render(request, 'todo_update.html', {'form': form, 'task': item})
