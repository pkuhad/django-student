from django.conf.urls.defaults import *

from students.index_classic.views import *

urlpatterns = patterns('students.index_classic.views',
    url(r'^$', 'index', name='index_view_classic'),
    url(r'^add_standard$', AddStandardView.as_view(), name='add_standard_classic'),
    url(r'^add_student$', AddStudentView.as_view(), name='add_student_classic'),
    url(r'^add_teacher$', AddTeacherView.as_view(), name='add_teacher_classic'),
)   

