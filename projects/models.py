from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    rollnum = models.IntegerField()
    rank = models.IntegerField()


class Projects(models.Model):
    sid = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    file_upload = models.FileField(upload_to="media")


    def __str__(self):
        return self.name