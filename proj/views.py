from django.views import View
from django.shortcuts import render

from proj.settings import INSTALLED_APPS

class BaseView(View):

    @staticmethod
    def _get_context():

        return {
            "title": "",
            "home": True,
            "text_buttons": [
                "Account",
                "Person",
                "Office"
            ],
            "apps": BaseView.__get_installed_apps(INSTALLED_APPS)

        }

    @staticmethod
    def __get_installed_apps(installed_settings_apps: list[str]):
        apps = installed_settings_apps[6:]

        return apps


class Home(BaseView):

    def get(self, request):
        return render(request, "proj/home.html", self.get_context())

    def get_context(self):
        context = self._get_context()

        return context
