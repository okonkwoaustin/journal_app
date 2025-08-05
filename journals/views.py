from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . models import Journal

class JournalList(ListView):
    """ List all the journals """
    model = Journal
    template_name = "journals/journal_list.html"
    context_object_name = "journals"

class JournalCreate(LoginRequiredMixin, CreateView):
    model = Journal
    template_name = "journals/journal_create.html"
    fields = "__all__"
    success_url = reverse_lazy("home")

    def form_invalid(self, form):
        form.instance.author = self.request.user
        return super().form_invalid(form)


class JournalDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Journal
    template_name = "journals/journal_detail.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class JournalUpdate(LoginRequiredMixin, UpdateView):
    model = Journal
    fields = "__all__"
    template_name = "journals/journal_update.html"
    success_url = reverse_lazy("home")
    
    def form_invalid(self, form):
        form.instance.author = self.request.user
        return super().form_invalid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
    
class JournalDelete(LoginRequiredMixin, DeleteView):
    model = Journal
    template_name = "journals/journal_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    