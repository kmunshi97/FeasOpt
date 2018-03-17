from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import *


def globals(request):
    context = {}

    return render(request, "globals/login.html", context)


def dashboard(request):
    context = {}
    if request.method == "GET":
        allTrucks = Truck.objects.all()
        allDrivers = Driver.objects.all()
        allCertificates = Certificates.objects.all()
        Notification.objects.all().delete()

        for truck in allTrucks:
            for cert in truck.certificates.all():
                daysLeft = cert.certificate.days_left


                if daysLeft <=30 and daysLeft >=0:
                    notfication = Notification(
                        truckNumber=truck.truckNumber,
                        driverName=truck.driverID.driverName,
                        certificateType=cert.certificate.certificateType,
                        daysLeft=cert.certificate.days_left,
                    )
                    notfication.save()

        allNotifications = Notification.objects.all()

        context = {
            'allNotifications': allNotifications,
            'allTrucks': allTrucks,
            'allDrivers': allDrivers,
            'allCertificates': allCertificates,
        }

    return render(request, "dashboard/dashboard.html", context)


def delete_notif(request):

    if request.is_ajax():
        notif = request.GET.get('notif')
        Notification.objects.get(id=notif).delete()
        return JsonResponse({'code': 200, 'message': 'success'})

    return Http404