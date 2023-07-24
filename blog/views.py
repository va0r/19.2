from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import Note


class NoteCreateView(CreateView):
    model = Note
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('blog:READ all')

    extra_context = {
        'title': 'Блог',
        'description': 'Создать запись'
    }


class NoteListView(ListView):
    model = Note

    extra_context = {
        'title': 'Блог',
        'description': 'Все записи'
    }


class NoteDetailView(DetailView):
    model = Note

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        note_item = Note.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = 'Блог'
        context_data['description'] = f'Запись {note_item.title.title()}'
        context_data['full'] = True
        return context_data


class NoteUpdateView(UpdateView):
    model = Note
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('blog:READ all')

    extra_context = {
        'title': 'Блог',
        'description': 'Редактировать запись'
    }


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('blog:READ all')
