from django.db import models

# Create your models here.


class Projects(models.Model):
    """ Creating model for the user """
    # i feel like we should link the model to the user using a 
    
    username = models.CharField(max_length=200)
    project_name = models.CharField(max_length=200)
    file_one = models.FileField(upload_to='media/file_one')
    file_two = models.FileField(upload_to='media/file_two')
    # output_file = models.FileField(upload_to= 'media/output_file')
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


