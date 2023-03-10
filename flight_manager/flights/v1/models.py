import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Airport(models.Model):
    iata_code = models.CharField(max_length=4, unique=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Flight(models.Model):
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="origin_airport"
    )
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="destination_airport"
    )
    flight_number = models.CharField(max_length=15)
    departure_date_time = models.DateTimeField()
    arrival_date_time = models.DateTimeField()
    baseFare = models.PositiveIntegerField()
    tax = models.PositiveIntegerField()
    provider = models.CharField(null=False, max_length=200)

    def __str__(self):
        return self.flight_number


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.id)


class ContactDetail(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    mobile_number = PhoneNumberField(null=False)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.email


class TravelerDetail(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    first_name = models.CharField(null=False, max_length=100)
    last_name = models.CharField(null=False, max_length=100)
    age = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.first_name
