from django import template
from notes_app.models import Comments

register = template.Library()

@register.filter(name='replace_tag')
def replace_tag(value, arg):
    return value.replace(arg, '')

@register.simple_tag
def comment_count(note):
    return Comments.objects.filter(comment_id=note).count()
