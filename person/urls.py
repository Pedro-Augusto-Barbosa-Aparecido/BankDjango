from django.urls import path
from .views import PersonListView, PersonCreateView, PersonDetailView, PersonEditView

urlpatterns = [
    path("", PersonListView.as_view(), name="person-list"),
    path("create", PersonCreateView.as_view(), name="person-create"),
    path("detail/<int:pk>", PersonDetailView.as_view(), name="person-detail"),
    path("edit/<int:pk>", PersonEditView.as_view(), name="person-edit")

]
