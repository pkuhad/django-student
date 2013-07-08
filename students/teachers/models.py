from django.db import models

from students.standards.models import Standard

class Teachers(models.Model):
    '''
    A student
    '''
    name                = models.CharField( max_length=200, help_text="Teacher Name", unique=True )
    description         = models.TextField( blank=True, null=True, help_text="Enter Any Description" ) 
    standard            = models.ManyToManyField( Standard, help_text="Teacher teaches in these standards" )

    def __unicode__(self):
        return self.name

