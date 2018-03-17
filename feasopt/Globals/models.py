from django.db import models
from datetime import date


CERTIFICATE_TYPE = (
    ('Fitness', 'Fitness'),
    ('Insurance', 'Insurance'),
    ('Pollution', 'Pollution'),
)


class Driver(models.Model):
    driverVerficationID = models.IntegerField(max_length=12)
    driverName = models.CharField(max_length=50)
    driverPhoneNumber = models.IntegerField(max_length=10)
    driverAddress = models.CharField(max_length=250)

    def __str__(self):
        return self.driverName


class Certificates(models.Model):
    certificateID = models.IntegerField()
    certificateType = models.CharField(max_length=15, choices=CERTIFICATE_TYPE)
    certificateIssueDate = models.DateField(default=date.today, null=False)
    certificateExpiryDate = models.DateField(null=False)

    @property
    def days_left(self):
        return (self.certificateExpiryDate - self.certificateIssueDate).days


class Truck(models.Model):
    truckNumber = models.CharField(max_length=15)
    driverID = models.ForeignKey(Driver, related_name="trucks", null=True, on_delete=models.SET_NULL)


class Holds_Certificate(models.Model):
    truck = models.ForeignKey(Truck, related_name='certificates', on_delete=models.CASCADE)
    certificate = models.ForeignKey(Certificates, on_delete=models.CASCADE)


class Notification(models.Model):
    truckNumber = models.CharField(max_length=15)
    driverName = models.CharField(max_length=50)
    certificateType = models.CharField(max_length=15, choices=CERTIFICATE_TYPE)
    daysLeft = models.IntegerField(default=-1, null=True)
    #viewed = models.BooleanField(default=False)
