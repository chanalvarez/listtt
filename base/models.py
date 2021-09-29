from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices




class Student(models.Model):
    Att_choice = (
        
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
        ('E', 'Excused'),
        ('D', 'Drop'),
        ('W', 'Withdraw'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Fullname = models.CharField(max_length=200)
    ID_no = models.CharField(max_length=11)
    Course_code = models.CharField(max_length=10)
    Attendance = models.CharField(max_length=200, choices= Att_choice)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Fullname

    class Meta:
        ordering = ['created']

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    section_name = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.section_name

    class Meta:
        ordering = ['complete']
