from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


#class LabInfo(models.Model):
 #   LabName = models.CharField(blank=True,max_length=20)
  #  LabCapacity = models.IntegerField(null=True)
  #  SoftwareInstalled = models.TextField(null=True)

    #def __str__(self):
      #  return self.LabName

class LabInf(models.Model):
    Name = models.CharField(blank=True,max_length=100)
    LabCapacity=models.IntegerField()
    Software=models.TextField()

    def __str__(self):
        return self.Name


class LabTeacher(models.Model):
    TeacherName = models.CharField(blank=True,max_length=20,primary_key=True)
    #Department = models.CharField(blank=True, max_length=20)
    Contact = models.IntegerField()

    def __str__(self):
        return self.TeacherName


class LabAttendent(models.Model):
    AttendentName = models.CharField(blank=True,max_length=20,primary_key=True)
    LabAssigned = models.TextField()
    Contact = models.IntegerField()

    def __str__(self):
        return self.AttendentName



class Complains(models.Model):
    LabName = models.ForeignKey(LabInf, on_delete=models.CASCADE)
    Issue = models.TextField()
    ResolvedValue = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)



class LabSchedule(models.Model):
    LabName =models.ForeignKey(LabInf, on_delete=models.SET_NULL, null=True,)
    TimeSlot = models.CharField(blank=True,max_length=7)
    Batch = models.CharField(blank=True,max_length=8)
    Day = models.CharField(blank=True,max_length=13)
    Subject = models.CharField(blank=True,max_length=10)
    TeacherName=models.ForeignKey(LabTeacher,on_delete = models.SET_NULL, null=True)


class Notice(models.Model):
        IssuedOn = models.DateField()
        Text = models.TextField()


#class FreeSlotBooking(models.Model):
 #   TimeSlot=models.ForeignKey(LabSchedule,on_delete=models.SET_NULL, null=True,related_name='Time')
  #  BookedBy=models.ForeignKey(LabTeacher,on_delete=models.SET_NULL, null=True)
   # Day=models.ForeignKey(LabSchedule,on_delete=models.SET_NULL, null=True,related_name='day')

