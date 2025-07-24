from django.urls import path
from .views import JournalList, JournalCreate, JournalDetail, JournalUpdate, DeleteView

urlpatterns = [
    path("", JournalList.as_view(), name="home"),
    path("create/", JournalCreate.as_view(), name="journal-create"),
    path("<int:pk>/", JournalDetail.as_view(), name="journal-detail"),
    path("<int:pk>/edit/", JournalUpdate.as_view(), name="journal-update"),
    #path("<int:pk>/delete", DeleteView.as_view(), name="journal-delete"),
]