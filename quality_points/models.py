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


class Point(models.Model):
    cre_hr = models.ForeignKey(CreditHour, on_delete=models.CASCADE, default=1)
    numbers = models.IntegerField()
    points = models.FloatField()

    def __str__(self):
        return str(self.points)