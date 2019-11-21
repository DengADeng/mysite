from django import template
from ..form import CommentForm
from ..models import Comments
register = template.Library()


@register.inclusion_tag('users/inclusions/_form.html', takes_context=True)
def show_comment_form(context, entry, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'entry': entry,
    }

@register.inclusion_tag('users/inclusions/_list.html', takes_context=True)
def show_comments(context, entry):
    comment_list = Comments.objects.filter(article=entry).order_by('-created_time') # entry.comment_set.all().order_by('-created_time')
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }