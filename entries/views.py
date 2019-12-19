from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Entry,Category
import markdown,markdown.extensions.codehilite


class HomeView(ListView):
    model = Entry
    template_name = 'entries/homepage.html'
    context_object_name = 'blog_entries'
    ordering = ['-entry_date']
    paginate_by = 3


def EntryView(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    entry.entry_text = markdown.markdown(entry.entry_text,
                                         extensions=[
                                             'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions.toc',
                                         ])
    return render(request, 'entries/entry_detail.html', context={'entry': entry})


def CategoryView(request):
    categories = Category.objects.all()
    entries = Entry.objects.all()
    return render(request, 'entries/category.html', {'categories': categories,'entries': entries})
'''
class CreateEntry(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'entries/create_entry1.html'
    fields = ['entry_title', 'entry_text', 'entry_excerpt', 'category', 'tags']

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)
'''