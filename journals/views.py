from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect
from django.db.models import Q

from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Journal
from .forms import JournalEntryForm


class JournalHome(TemplateView):
    "Landing page for Journal"
    template_name = "journals/home.html"
    

class JournalList(LoginRequiredMixin, ListView):
    """List all the journals"""

    model = Journal
    template_name = "journals/journal_list.html"
    context_object_name = "journals"
    paginate_by = 4

    def get_queryset(self):
        user = self.request.user
        # Show public journals OR private journals owned by this user
        return Journal.objects.filter(
            Q(is_private=False) | Q(author=user)
        )


class JournalCreate(LoginRequiredMixin, CreateView):
    model = Journal
    template_name = "journals/journal_create.html"
    form_class = JournalEntryForm
    success_url = reverse_lazy("journal-list")
    
    def form_valid(self, form):
        # attach the logged-in user before saving
        form.instance.author = self.request.user
        return super().form_valid(form)


class JournalDetail(LoginRequiredMixin, DetailView):
    model = Journal
    template_name = "journals/journal_detail.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


from django.shortcuts import redirect

class JournalUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Journal
    form_class = JournalEntryForm
    template_name = "journals/journal_update.html"
    success_url = reverse_lazy("journal-list")

    def form_invalid(self, form):
        form.instance.author = self.request.user
        return super().form_invalid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



class JournalDelete(LoginRequiredMixin, DeleteView):
    model = Journal
    template_name = "journals/journal_delete.html"
    success_url = reverse_lazy("journal-list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
