from django.shortcuts import render
from django.views import View

from .models import Person

# Create your views here.


class PersonListView(View):

    def get(self, request):
        return render(request, "person-list.html", self.get_context())

    def get_context(self):
        return {
            "home": False,
            "objects": self.get_objects(),
            "title": "Person List Page",
            "text_buttons": [
                "Account",
                "Person",
                "Office"
            ]

        }

    def get_objects(self):
        qs = Person.objects.all()

        return qs
