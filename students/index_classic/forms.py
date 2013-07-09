from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from students.standards.models import Standard
from students.students.models import Student
from students.teachers.models import Teachers

class AddStandardForm(ModelForm):
    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'post'
    helper.add_input(Submit('submit', 'Create Standard'))

    class Meta:
        model = Standard

class AddStudentForm(ModelForm):
    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'post'
    helper.add_input(Submit('submit', 'Create Student'))

    class Meta:
        model = Student
 
class AddTeacherForm(ModelForm):
    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'post'
    helper.add_input(Submit('submit', 'Create Student'))

    class Meta:
        model = Teachers
