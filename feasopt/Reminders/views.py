from django.shortcuts import render


def reminders(request):
    context = {}

    return render(request, "reminders/reminders.html", context)
