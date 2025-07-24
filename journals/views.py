from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
    success_url = "http://127.0.0.1:8000/"


class JournalDetail(DetailView):
    model = Journal
    template_name = "journals/journal_detail.html"

class JournalUpdate(UpdateView):
    model = Journal
    template_name = "journals/journal_update.html"
    fields = "__all__"
    success_url = "http://127.0.0.1:8000/"
    
""" class JournalDelete(DeleteView):
    model = Journal
    template_name = "journals/journal_delete.html"
    success_url = reverse_lazy('journal_list') """