from django.shortcuts import render
from django.views import View

# Create your views here.


class PersonListView(View):

    def get(self, request):
        return render(request, "person-list.html", {})
