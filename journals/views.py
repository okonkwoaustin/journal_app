from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy, reverse

from . models import Journal

class JournalList(ListView):
    """ List all the journals """
    model = Journal
    template_name = "journals/journal_list.html"
    context_object_name = "journals"

class JournalCreate(CreateView):
    model = Journal
    template_name = "journals/journal_create.html"
    fields = "__all__"
    success_url = reverse_lazy("home")


class JournalDetail(DetailView):
    model = Journal
    template_name = "journals/journal_detail.html"

class JournalUpdate(UpdateView):
    model = Journal
    template_name = "journals/journal_update.html"
    fields = "__all__"
    
    def get_success_url(self):
        return reverse('journal-detail', kwargs={'pk': self.object.pk})
    
class JournalDelete(DeleteView):
    model = Journal
    template_name = "journals/journal_delete.html"
    success_url = reverse_lazy("home")