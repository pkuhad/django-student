from django.db import models

from students.standards.models import Standard
from students.teachers.models import Teachers

class Student(models.Model):
    '''
    A student
    '''
    name                = models.CharField( max_length=200, help_text="Enter Student Name", unique=True )
    description         = models.TextField( blank=True, null=True, help_text="Enter Any Description" ) 
    standard            = models.ForeignKey( Standard, help_text="Student's Standard", related_name="standard" )
    mentored_by         = models.ForeignKey( Teachers, blank=True, null=True, help_text="Student is mentored by", related_name="mentored_students" )

    def __unicode__(self):
        return self.name

