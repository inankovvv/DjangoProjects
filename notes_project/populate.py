import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notes_project.settings')

import django
django.setup()

from notes_app.models import Notes
from faker import Faker

faked = Faker()

def dummy_notes(n=5):

    for entry in range(n):
        note_name = faked.sentence()
        note_note = ' '.join(faked.sentences())
        note_date = faked.date()
        note_time = faked.time()
        note = Notes.objects.get_or_create(title=note_name, note=note_note, date=note_date, time=note_time)[0]


if __name__ == '__main__':
    print('Running populate script')
    dummy_notes(20)
    print('Populating dummy notes done!')
