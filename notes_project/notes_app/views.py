from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, time
from notes_app.models import Notes, Categories, Comments
from notes_app.forms import NoteForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required()
def single_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id)
    all_comments = Comments.objects.filter(comment_id=note)

    comment = add_comment(request, note)
    if request.method == 'POST':
        return redirect('notes_app:note', note_id=note_id)

    context = {
        'note': note,
        'all_comments': all_comments,
        'comment_form': comment,
    }
    return render(request, 'notes_app/single_note.html', context)


def my_notes(request, category = None, done = None):
    all_notes = Notes.objects.order_by('-date', '-time')

    if category:
        category_is = get_object_or_404(Categories, name=category)
        all_notes = all_notes.filter(category__name=category_is)

    if done:
        if done == 'done':
            all_notes = all_notes.filter(done=True)
        elif done == 'pending':
            all_notes = all_notes.filter(done=False)

    page = request.GET.get('page', 1)
    paginator = Paginator(all_notes, 5)
    try:
        all_notes = paginator.page(page)
    except PageNotAnInteger:
        all_notes = paginator.page(1)
    except EmptyPage:
        all_notes = paginator.page(paginator.num_pages)

    notes_html = {
        'all_notes': all_notes,
        'categories': Categories.objects.all(),
        'current_category': category
    }
    return render(request, 'notes_app/my_notes.html', notes_html)

@login_required()
def add_note(request):
    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.posted_by = request.user
            new_note.save()
            return redirect('notes_app:note', note_id=new_note.id)

    return render(request, 'notes_app/add_note.html', {'form': form})

@login_required()
def update_note(request, note_id):

    form = NoteForm()
    context = {}
    obj = get_object_or_404(Notes, id = note_id)
    form = NoteForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('notes_app:note', note_id=note_id)

    context['form'] = form

    return render(request, 'notes_app/update_note.html', context)

@login_required()
def update_note_done(request, note_id):
    note = get_object_or_404(Notes, id=note_id)
    note.update_done()
    return redirect('notes_app:note', note_id=note_id)

@login_required()
def delete_note(request, note_id):

    obj = get_object_or_404(Notes, id = note_id)

    if request.method == 'POST':
        obj.delete()
        return redirect('notes_app:my_notes')

    return render(request, 'notes_app/delete_note.html', {'note': obj})

@login_required()
def add_comment(request, note):
    comment = CommentForm(request.POST or None)
    if comment.is_valid():
        comment_instance = comment.save(commit=False)
        comment_instance.comment_id = note
        comment_instance.posted_by = request.user
        comment_instance.save()
    return comment
