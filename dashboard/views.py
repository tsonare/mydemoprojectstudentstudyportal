from django.shortcuts import render,get_object_or_404
from .models import Note, Homework, Todo
from .forms import *
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.


def home_authenticated(request):
    return render(request, 'dashboard/home_authenticated.html')


def home_not_authenticated(request):
    return render(request, 'dashboard/home_not_authenticated.html')


# Note section


class NoteCreateView(SuccessMessageMixin,CreateView):
    template_name = 'dashboard/notes.html'
    model = Note
    fields = ['title','description']
    success_url = reverse_lazy('display_notes')
    success_message = "Note Saved Successfully."
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(NoteCreateView, self).form_valid(form)


class NoteDisplayView(ListView):
    model = Note
    paginate_by = 12
    template_name = 'dashboard/notes_display.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        note = Note.objects.filter(user = self.request.user )
        context = {'note': note}
        return context


class NoteDetailView(DetailView):
    model =  Note
    template_name = 'dashboard/notes_detail.html'
    def detail_note(request,pk):
        note = get_object_or_404(Note, id=pk)
        

class NoteUpdateView(SuccessMessageMixin,UpdateView):
    model = Note
    template_name = 'dashboard/note_update.html'
    fields = ['title','description'] 
    success_url = reverse_lazy('display_notes')
    success_message = "Note Updated successfully."
    def update_note(request,pk):
        note = get_object_or_404(Note, id=pk)
    # def get_success_url(self):
    #     return reverse_lazy('display_notes') # Message With function


class NoteDeleteView(SuccessMessageMixin,DeleteView):
    model = Note
    template_name = 'dashboard/note_delete.html'
    success_messages = "Note Delete Successfully."
    success_url = reverse_lazy('display_notes')
    def delete_note(request,pk):
        note = get_object_or_404(Note, id=pk)

    
# Homework section


class HomeworkCreateView(SuccessMessageMixin,CreateView):
    model = Homework
    template_name = 'dashboard/homework.html'
    fields = ['subject','title','description','due_date','status']
    success_url = reverse_lazy('display_homework')
    success_message = "Homework Saved Successfully."
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(HomeworkCreateView, self).form_valid(form)


class HomeworkDisplayView(ListView):
    model = Homework
    paginate_by = 12
    template_name = 'dashboard/homework_display.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        homework = Homework.objects.filter(user = self.request.user )
        context = {'homework': homework}
        return context


class HomeworkDetailView(SuccessMessageMixin,DetailView):
    model =  Homework
    template_name = 'dashboard/homework_detail.html'
    def detail_homework(request,pk):
        homework = get_object_or_404(Homework, id=pk)


class HomeworkUpdateView(SuccessMessageMixin,UpdateView):
    model = Homework
    template_name = 'dashboard/homework_update.html'
    fields = ['subject','title','description','due_date','status'] 
    success_url = reverse_lazy('display_homework')
    success_message = "Homework Updated successfully."
    def update_homework(request,pk):
        homework = get_object_or_404(Homework, id=pk)


class HomeworkDeleteView(SuccessMessageMixin,DeleteView):
    model = Homework
    template_name = 'dashboard/homework_delete.html'
    success_messages = "Homework Delete Successfully."
    success_url = reverse_lazy('display_homework')
    def delete_homework(request,pk):
        homework = get_object_or_404(Homework, id=pk)
    

# To do section


class TodoCreateView(SuccessMessageMixin,CreateView):
    model = Todo
    template_name = 'dashboard/todo.html'
    fields = ['title','todo_status']
    success_url = reverse_lazy('display_todo')
    success_message = 'Todo List Created successfully.'
    def form_valid(self,form):
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(TodoCreateView, self).form_valid(form)


class TodoDisplayView(ListView):
    model = Todo
    paginate_by = 20
    template_name = 'dashboard/todo_display.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todo = Todo.objects.filter(user = self.request.user )
        context = {'todo': todo}
        return context


class TodoUpdateView(SuccessMessageMixin,UpdateView):
    model = Todo
    template_name = 'dashboard/todo_update.html'
    fields = ['title','todo_status'] 
    success_url = reverse_lazy('display_todo')
    success_message = "Todo List Updated successfully."
    def update_todo(request,pk):
        todo = get_object_or_404(Todo, id=pk)


class TodoDeleteView(SuccessMessageMixin,DeleteView):
    model = Todo
    template_name = 'dashboard/todo_delete.html'
    success_messages = "Todo Deleted Successfully."
    success_url = reverse_lazy('display_todo')
    def delete_todo(request,pk):
        homework = get_object_or_404(Todo, id=pk)



