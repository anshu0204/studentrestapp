from django.db import models

class StudentDetails(models.Model):
    name = models.CharField(max_length=40)
    rollNo = models.BigIntegerField(primary_key=True)
    marks_subject1=models.IntegerField()
    marks_subject2=models.IntegerField()
    marks_subject3=models.IntegerField()

class CSVFile(models.Model):
    CSVFile = models.FileField()    