from django.db import models

class Standard(models.Model):
    '''
    A School's different standards/classes
    '''
    level         = models.CharField( max_length=2, help_text="Enter Standard Digit" )
    description   = models.TextField( blank=True, null=True, help_text="Enter Any Description" ) 

    def __unicode__(self):
        return self.level


