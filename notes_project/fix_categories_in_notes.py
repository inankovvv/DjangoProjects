import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notes_project.settings')

import django
django.setup()

from notes_app.models import Notes, Categories

# all_notes = Notes.objects.all()
#
# for note in all_notes:
#     note.category = 1
#
# category = Categories(id=1, name='Primary Category', description='For all notes by default')
# category.save()

categories = Categories.objects.all()

print(categories)
