from django.http import HttpResponse
from django.shortcuts import render


def automation_home(request):
    context = {}
    return render(request, "automations/automation_home.html", context)


def add_automation(request):
    context = {}
    return HttpResponse("Add automation")


def details_automation(request, pk):
    context = {}
    return HttpResponse("Details automation")


def edit_automation(request, pk):
    context = {}
    return HttpResponse("Edit automation")


def delete_automation(request, pk):
    context = {}
    return HttpResponse("Delete automation")
