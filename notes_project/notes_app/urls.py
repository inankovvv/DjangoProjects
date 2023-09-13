from django.urls import path
from notes_app import views

app_name = 'notes_app'

urlpatterns = [
    path('', views.my_notes, name='index'),
    path('my_notes/', views.my_notes, name='my_notes'),
    path('my_notes/filter/<str:category>', views.my_notes, name='filter_notes'),
    path('my_notes/filter/<str:category>/<str:done>', views.my_notes, name='filter_notes'),
    path('my_notes/add_note', views.add_note, name='add_note'),
    path('my_notes/note/<int:note_id>', views.single_note, name='note'),
    path('my_notes/update_note/<int:note_id>', views.update_note, name='update_note'),
    path('my_notes/delete_note/<int:note_id>', views.delete_note, name='delete_note'),
    path('my_notes/note_done/<int:note_id>', views.update_note_done, name='update_note_done')
]
