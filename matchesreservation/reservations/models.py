from django.db import models
from django.utils import timezone


class Stadium(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField(null=False)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} {self.capacity} places'


class Match(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.date}'


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name} {self.email}'


class Ticket(models.Model):
    reservdate = models.DateTimeField(timezone.now)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.FloatField()


