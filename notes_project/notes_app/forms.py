from django.forms import ModelForm
from notes_app.models import Notes, Comments

class NoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'note', 'category']

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
