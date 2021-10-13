from django.urls import path
from .views import PersonListView, PersonCreateView, PersonDetailView

urlpatterns = [
    path("", PersonListView.as_view(), name="person-list"),
    path("create", PersonCreateView.as_view(), name="person-create"),
    path("detail/<int:pk>", PersonDetailView.as_view(), name="person-detail")

]
