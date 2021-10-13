from django.shortcuts import render
from django.views import View

from dashboards.views import BaseView

from .models import Person

# Create your views here.


class PersonListView(BaseView):

    def get(self, request):
        return render(request, "person-list.html", self.get_context())

    def get_context(self):
        context = self._get_context()
        context["home"] = False
        context["objects"] = self.get_objects()
        context["fields"] = [
            "Name", "Email", "Active", "Gender"
        ]

        return context

    def get_objects(self):
        qs = Person.objects.all()

        return qs


class PersonCreateView(BaseView):

    def get(self, request):
        return render(request, "person-create.html", self.get_context())

    def get_context(self):
        context = self._get_context()
        context["title"] = "Person Create"
        context["home"] = False

        return context


class PersonDetailView(BaseView):

    def get(self, request, pk):
        return render(request, 'person-detail.html', self.get_context(pk))

    def get_context(self, pk):
        context = self._get_context()
        context["title"] = "Person Detail"
        context["home"] = False
        context["person"] = self.get_qs(pk)[0]

        return context

    def get_qs(self, pk):
        return Person.objects.all().filter(pk=pk)
