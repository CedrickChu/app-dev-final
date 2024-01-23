from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Manga
from .forms import MangaForm
from django.urls import reverse_lazy


class MangaListView(ListView):
    model = Manga
    template_name = 'manga_list.html'
    context_object_name = 'mangas'

class MangaDetailView(DetailView):
    model = Manga
    template_name = 'manga_detail.html'

class MangaCreateView(CreateView):
    model = Manga
    form_class = MangaForm
    template_name = 'manga_form.html'

class MangaUpdateView(UpdateView):
    model = Manga
    form_class = MangaForm
    template_name = 'manga_form.html'
    def get_success_url(self):
        # You can add more logic here if needed
        return reverse_lazy('manga-list')

class MangaDeleteView(DeleteView):
    model = Manga
    template_name = 'manga_confirm_delete.html'
    success_url = 'manga-list'