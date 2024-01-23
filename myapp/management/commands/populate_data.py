from django.core.management.base import BaseCommand
from myapp.models import Genre

class Command(BaseCommand):
    help = 'Populates the Genre model with predefined genres.'

    def handle(self, *args, **kwargs):
        genres = ['Action', 'Adventure', 'Comedy', 'Cooking', 'Doujinshi', 'Drama', 'Erotica', 'Fantasy', 'Gender bender', 'Harem', 'Historical', 'Horror', 'Isekai', 'Josei', 'Manhua', 'Manhwa', 'Martial arts', 'Mature', 'Mecha', 'Medical', 'Mystery', 'One shot', 'Pornographic', 'Psychological', 'Romance', 'School life', 'Sci fi', 'Seinen', 'Shoujo', 'Shoujo ai', 'Shounen', 'Shounen ai', 'Slice of life', 'Smut', 'Sports', 'Supernatural', 'Tragedy', 'Webtoons', 'Yaoi', 'Yuri']

        for genre_name in genres:
            Genre.objects.create(genre_name=genre_name)

        self.stdout.write(self.style.SUCCESS('Successfully populated the Genre model.'))