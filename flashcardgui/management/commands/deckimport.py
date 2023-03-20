
from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll
from api.models import Deck, Flashcard

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for poll_id in options['poll_ids']:
            try:
                #poll = Poll.objects.get(pk=poll_id)
                decks = Deck.objects.get()
            except Deck.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))



