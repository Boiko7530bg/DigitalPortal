from django.http import HttpResponse
from django.shortcuts import render


def add_tracker(request):
    context = {}
    return HttpResponse("Add tracker")


def details_tracker(request, pk):
    context = {}
    return HttpResponse("Details tracker")


def edit_tracker(request, pk):
    context = {}
    return HttpResponse("Edit tracker")


def delete_tracker(request, pk):
    context = {}
    return HttpResponse("Delete tracker")
