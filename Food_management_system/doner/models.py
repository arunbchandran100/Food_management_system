from django.db import models

class DonateFoodModel(models.Model):
    choice1=[
       ("Hotel","Hotel"),
       ("Catering","catering"),
       ("Hostels","Hostels"),
       ("Normal user","Normal user")
    ]
    choice2=[
        ("biriyani","biriyani"),
        ("rice","rice"),
        ("porota curry","porota curry"),
        ("puttu curry","puttu curry")
    ]
    choice3=[
        ("veg","veg"),
        ("Nonveg","Nonveg"),
        ("Both","Both")
    ]
    user=models.CharField(max_length=120)
    donor_type=models.CharField(max_length=100,choices=choice1)
    donor_discription=models.CharField(max_length=100)
    food_type=models.CharField(max_length=100,choices=choice3)
    food=models.CharField(max_length=100,choices=choice2)
    food_discription=models.CharField(max_length=100)
    date=models.DateTimeField()
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.user


class FeedbackModel(models.Model):
    user=models.CharField(max_length=120)
    feedback=models.CharField(max_length=200)
    def __str__(self):
        return self.user