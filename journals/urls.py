from django.urls import path
from .views import JournalList, JournalCreate, JournalDetail

urlpatterns = [
    path("", JournalList.as_view(), name="home"),
    path("create/", JournalCreate.as_view(), name="journal-create"),
    path("<int:pk>/", JournalDetail.as_view(), name="journal-detail"),
]