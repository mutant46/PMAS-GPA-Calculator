from django.db import models

# Create your models here.

class CreditHour(models.Model):
    hours = models.IntegerField()

    def __str__(self):
        return str(self.hours)

class HighestNumber(models.Model):
    belongs_to = models.ForeignKey(CreditHour, related_name='highest', on_delete=models.CASCADE, default=1)
    highest = models.IntegerField()

    def __str__(self):
        return str(self.highest)


class Number(models.Model):
    credit_hour = models.ForeignKey(CreditHour, related_name='number', on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)


class Point(models.Model):
    numbers = models.ForeignKey(Number, related_name='points', on_delete=models.CASCADE)
    points = models.FloatField()

    def __str__(self):
        return str(self.points)