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

class OrdersModel(models.Model):
    donor=models.CharField(max_length=120)
    donor_type=models.CharField(max_length=100)
    donor_discription=models.CharField(max_length=100)
    food_type=models.CharField(max_length=100)
    food=models.CharField(max_length=100)
    food_discription=models.CharField(max_length=100)
    date=models.DateTimeField()
    location=models.CharField(max_length=100)
    user=models.CharField(max_length=120)
    count = models.PositiveIntegerField()
    description = models.TextField()
    contact_information = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user
