from django.shortcuts import render

from dashboards.views import BaseView


class Home(BaseView):

    def get(self, request):
        return render(request, "proj/home.html", self.get_context())

    def get_context(self):
        context = self._get_context()

        return context
