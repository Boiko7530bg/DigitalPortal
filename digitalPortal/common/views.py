from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    contex = {"title": "Digital portal"}
    return render(request, "common/index.html", contex)
