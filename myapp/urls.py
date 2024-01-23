from django.urls import path
from .views import MangaListView, MangaDetailView, MangaCreateView, MangaUpdateView, MangaDeleteView

urlpatterns = [
    path('mangas/', MangaListView.as_view(), name='manga-list'),
    path('manga/<int:pk>/', MangaDetailView.as_view(), name='manga-detail'),
    path('manga/new/', MangaCreateView.as_view(), name='manga-create'),
    path('manga/<int:pk>/edit/', MangaUpdateView.as_view(), name='manga-update'),
    path('manga/<int:pk>/delete/', MangaDeleteView.as_view(), name='manga-delete'),
]