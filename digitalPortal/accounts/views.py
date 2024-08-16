from django.http import HttpResponse
from django.shortcuts import render, redirect


def signup_user(request):
    context = {}
    return render(request, "accounts/signup_user.html", context)


def signin_user(request):
    context = {}
    return render(request, "accounts/signin_user.html", context)


def signout_user(request):
    context = {}
    return HttpResponse("Sign out user")


def details_user(request, pk):
    context = {}
    return HttpResponse("Details user")


def edit_user(request, pk):
    context = {}
    return HttpResponse("Edit user")


def delete_user(request, pk):
    context = {}
    return HttpResponse("Delete user")
