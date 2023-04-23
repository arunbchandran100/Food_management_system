from django.db import models
# from datetime import datetime

# Create your models here.
class DonateFood(models.Model):
    # user=models.CharField(max_length=100)
    food_type=models.CharField(max_length=100)
    discription=models.TextField()
    supply_date=models.DateField()
    pickup_location=models.CharField(max_length=100)
    pickup_deadline=models.DateField()
    contact_information=models.CharField(max_length=100)
    def __str__(self):
        return self.user


