from django.urls import path
from .views import JournalList, JournalCreate, JournalDetail, JournalUpdate, JournalDelete

urlpatterns = [
    path("", JournalList.as_view(), name="home"),
    path("create/", JournalCreate.as_view(), name="journal-create"),
    path("<int:pk>/", JournalDetail.as_view(), name="journal-detail"),
    path("edit/<int:pk>/", JournalUpdate.as_view(), name="journal-update"),
    path("delete/<int:pk>/", JournalDelete.as_view(), name="journal-delete"),
]