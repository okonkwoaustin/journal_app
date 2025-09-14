from django.urls import path
from .views import (
    JournalHome,
    JournalList,
    JournalCreate,
    JournalDetail,
    JournalUpdate,
    JournalDelete,
)

urlpatterns = [
    path("", JournalHome.as_view(), name="home"),
    path("list/", JournalList.as_view(), name="journal-list"),
    path("create/", JournalCreate.as_view(), name="journal-create"),
    path("<uuid:pk>/", JournalDetail.as_view(), name="journal-detail"),
    path("edit/<uuid:pk>/", JournalUpdate.as_view(), name="journal-update"),
    path("delete/<uuid:pk>/", JournalDelete.as_view(), name="journal-delete"),
]
