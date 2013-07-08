from django.conf.urls.defaults import *

urlpatterns = patterns('students.index_classic.views',
    url(r'^$', 'index', name='index_view_classic'),
    url(r'^add_student$', 'add_student', name='add_student_classic'),
)   

