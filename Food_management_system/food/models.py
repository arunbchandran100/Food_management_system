from django.db import models

class RequestDonation(models.Model):
    user=models.CharField(max_length=120)
    count = models.PositiveIntegerField()
    description = models.TextField()
    request_date = models.DateField()
    location = models.CharField(max_length=100)
    deadline = models.DateField()
    contact_information = models.CharField(max_length=100)

    def __str__(self):
        return self.user


