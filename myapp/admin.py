from django.contrib import admin
from .models import Status, Genre, Manga

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_name', 'created_at', 'updated_at')
    search_fields = ('status_name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre_name', 'created_at', 'updated_at')
    search_fields = ('genre_name',)

@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genres', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    filter_horizontal = ('genre',)  # Enables the "Add Another" button for Genre

    def display_genres(self, obj):
        return ", ".join([genre.genre_name for genre in obj.genre.all()])
    
    display_genres.short_description = 'Genres'