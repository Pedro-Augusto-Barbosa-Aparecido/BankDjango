from django.shortcuts import render
from django.views import View

# Create your views here.


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
            ]

        }
