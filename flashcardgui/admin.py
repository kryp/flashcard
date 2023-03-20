from django.contrib import admin
from api.models import Deck, Flashcard


class DeckAdmin(admin.ModelAdmin):
        pass

admin.site.register(Deck, DeckAdmin)
admin.site.register(Flashcard)