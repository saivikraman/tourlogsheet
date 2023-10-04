from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Datas(models.Model): 
    EmpCode= models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    SALUTATION_CHOICES = [
        ('Mr', 'Mr'),
        ('Ms', 'Ms'),
    ]
    salutation = models.CharField(max_length=2, choices=SALUTATION_CHOICES,null=True)    
    Desg = models.CharField(max_length=50)
    Grade_Pay = models.CharField(max_length=50)  
    Age=models.IntegerField()
    Email_ID=models.CharField(max_length=100)
    Phone = models.CharField(max_length=10,default='')
    Mobile=models.IntegerField()
    Office_Address=models.CharField(max_length=100)
    Purpose_of_Tour=models.CharField(max_length=100)
    Project_Expenditure = models.BooleanField(default=False)
    NICSI_Expenditure = models.BooleanField(default=False)
    Project_No=models.CharField(max_length=50)
    no = models.BooleanField(default=False)
    yes = models.BooleanField(default=False)
    Rs = models.CharField(max_length=100, null=True, blank=True)
    travel_date1 = models.CharField(max_length=255,default='')
    from_place1 = models.CharField(max_length=255,default='')
    to_place1 = models.CharField(max_length=255,default='')
    mode_of_travel1 = models.CharField(max_length=255,default='')
    flight_number1 = models.CharField(max_length=20,default='')
    departure_date1 = models.CharField(max_length=255,default='')
    departure_time1 = models.CharField(max_length=255,default='')
    arrival_date1 = models.CharField(max_length=255,default='')
    arrival_time1 = models.CharField(max_length=255,default='')
    travel_date2 = models.CharField(max_length=255,default='')
    from_place2 = models.CharField(max_length=255,default='')
    to_place2 = models.CharField(max_length=255,default='')
    mode_of_travel2 = models.CharField(max_length=255,default='')
    flight_number2 = models.CharField(max_length=20,default='')
    departure_date2 = models.CharField(max_length=255,default='')
    departure_time2 = models.CharField(max_length=255,default='')
    arrival_date2 = models.CharField(max_length=255,default='')
    arrival_time2 = models.CharField(max_length=255,default='')
    travel_date3 = models.CharField(max_length=255,default='')
    from_place3 = models.CharField(max_length=255,default='')
    to_place3 = models.CharField(max_length=255,default='')
    mode_of_travel3 = models.CharField(max_length=255,default='')
    flight_number3 = models.CharField(max_length=20,default='')
    departure_date3 = models.CharField(max_length=255,default='')
    departure_time3 = models.CharField(max_length=255,default='')
    arrival_date3 = models.CharField(max_length=255,default='')
    arrival_time3 = models.CharField(max_length=255,default='')
    travel_date4 = models.CharField(max_length=255,default='')
    from_place4 = models.CharField(max_length=255,default='')
    to_place4 = models.CharField(max_length=255,default='')
    mode_of_travel4 = models.CharField(max_length=255,default='')
    flight_number4 = models.CharField(max_length=20,default='')
    departure_date4 = models.CharField(max_length=255,default='')
    departure_time4 = models.CharField(max_length=255,default='')
    arrival_date4 = models.CharField(max_length=255,default='')
    arrival_time4 = models.CharField(max_length=255,default='')
    travel_date5 = models.CharField(max_length=255,default='')
    from_place5 = models.CharField(max_length=255,default='')
    to_place5 = models.CharField(max_length=255,default='')
    mode_of_travel5 = models.CharField(max_length=255,default='')
    flight_number5 = models.CharField(max_length=20,default='')
    departure_date5 = models.CharField(max_length=255,default='')
    departure_time5 = models.CharField(max_length=255,default='')
    arrival_date5 = models.CharField(max_length=255,default='')
    arrival_time5 = models.CharField(max_length=255,default='')
    


class Detail(models.Model):
    Name = models.CharField(max_length=100)
    Emp = models.CharField(max_length=100)
