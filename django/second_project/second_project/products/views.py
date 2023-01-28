from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html",{})


def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 1234,
        "my_list": [123,1234,12345]
    }
    return render(request, "contact.html", my_context)