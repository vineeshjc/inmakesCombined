from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView

from django.views.generic.detail import DetailView

from django.views.generic.edit import DeleteView, UpdateView

from todo_app.models import todo_db

def todo_add(request):
    item = todo_db.objects.all()
    if request.method == 'POST':
        name = request.POST.get('todo',)
        level = request.POST.get('level',)
        created = request.POST.get('created',)
        todo = todo_db(name=name, level=level, created=created)
        todo.save()
        return redirect('todo_class:todo_list')
    return render(request, 'todo_list_class.html', dict(data=item))

class todo_list(ListView):
    model = todo_db
    template_name = 'todo_list_class.html'
    context_object_name = 'data'


class todo_details(DetailView):
    model = todo_db
    template_name = 'todo_class_detail_view.html'
    context_object_name = 'data'

class todo_delete(DeleteView):
    model = todo_db
    template_name = 'todo_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('todo_class:todo_list')

class todo_update(UpdateView):
    model = todo_db
    template_name = 'todo_update.html'
    context_object_name = 'task'
    fields =['name', 'level', 'created']

    def get_success_url(self):
        return reverse_lazy('todo_class:todo_details', kwargs={'pk': self.object.id})


