from django.shortcuts import render


def globals(request):
    context = {}

    return render(request, "globals/login.html", context)


def dashboard(request):
    context = {}

    return render(request, "dashboard/dashboard.html", context)
