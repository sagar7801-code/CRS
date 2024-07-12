from django.db import models
import math
from django.utils import timezone
from datetime import datetime

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 20)
    otp = models.IntegerField(default = 459)
    status = models.CharField(default = "Pending",max_length = 7)
    is_activate = models.BooleanField(default = True)
    is_verified = models.BooleanField(default = False)
    role = models.CharField(max_length = 20)
    created_at = models.DateTimeField(default = datetime.now,blank = False,max_length = 12)
    updated_at = models.DateTimeField(auto_now = True,blank = False)

    def __str__(self):
        return self.email

class College(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length = 80)
    f_name = models.CharField(max_length = 20)
    l_name = models.CharField(max_length = 20)
    contact = models.CharField(max_length = 10)
    address = models.CharField(max_length = 100,blank = True)
    c_picture = models.FileField(upload_to = 'img/',blank = True,default = "img/def.jpg")

    def __str__(self):
        return self.user_id.email

class Company(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    hr_f_name = models.CharField(max_length = 20)
    hr_l_name = models.CharField(max_length = 20)
    address = models.CharField(max_length = 200)
    contact = models.CharField(max_length = 10)
    url = models.CharField(max_length = 200)
    about = models.CharField(max_length = 1500,blank = True)
    owner = models.CharField(max_length = 20)
    reg_date = models.CharField(default = datetime.now,blank = False,max_length = 12)
    picture = models.FileField(upload_to = 'img/',blank = True,default = "img/def.jpg")

    def __str__(self):
        return self.name
    
class Student(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    enroll = models.CharField(max_length = 12)
    f_name = models.CharField(max_length = 20)
    l_name = models.CharField(max_length = 20)
    contact = models.CharField(max_length = 10)
    address = models.CharField(max_length = 150)
    gender = models.CharField(max_length = 10)
    dob = models.DateField(blank = True)
    remarks = models.CharField(max_length = 150)
    degree = models.CharField(max_length = 50)
    status = models.CharField(max_length = 10)
    reg_date = models.DateTimeField(default = datetime.now,blank = False,max_length = 12)
    resume = models.FileField(upload_to = 'resume',blank = True,default = "")
    s_picture = models.FileField(upload_to = 'img/',blank = True,default = "img/def.jpg")

    def __str__(self):
        return self.user_id.email
    
class Vacancy(models.Model):
    com_id = models.ForeignKey(Company,on_delete = models.CASCADE)
    language = models.CharField(max_length = 10)
    date = models.DateField(blank = False,max_length = 12)
    vac_count = models.CharField(max_length = 5)

    def __str__(self):
        return self.com_id.user_id.email

    def whenpublished(self):
        now = timezone.now()  
        diff= now - self.date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"
            
class Suggetion(models.Model):
    s_id = models.ForeignKey(Student,on_delete = models.CASCADE)
    date = models.DateTimeField(default = datetime.now,blank = False,max_length = 12)
    subject = models.CharField(max_length = 50)
    messege = models.CharField(max_length = 500)

    def __str__(self):
        return self.s_id.user_id.email
    
    def whenpublished(self):
        now = timezone.now()  
        diff= now - self.date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            if seconds == 1:
                return str(seconds) +  "second ago"
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            if minutes == 1:
                return str(minutes) + " minute ago"
            else:
                return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            if hours == 1:
                return str(hours) + " hour ago"
            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
            if days == 1:
                return str(days) + " day ago"
            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"

        if diff.days >= 365:
            years= math.floor(diff.days/365)
            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

class Apply(models.Model):
    com_id = models.ForeignKey(Company,on_delete = models.CASCADE)
    s_id = models.ForeignKey(Student,on_delete = models.CASCADE)
    status = models.CharField(max_length = 10 , default = "Pending")

    def __str__(self):
        return self.s_id.user_id.email

class Interview(models.Model):
    a_id = models.ForeignKey(Apply,on_delete = models.CASCADE)
    date = models.DateField(blank = False)
    time = models.TimeField(blank = False)
    status = models.CharField(max_length = 200 , default = "Pending")

    def __str__(self):
        return self.a_id.s_id.user_id.email