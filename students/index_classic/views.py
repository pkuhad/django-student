import logging

from django.conf import settings
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from django.views.generic.base import View
from students.index_classic.forms import *
from students.standards.models import Standard

def index(request):
    '''
    Handles the index request of application. When logged in it redirects to /home
    '''
    return render_to_response('index/index.html', context_instance = RequestContext(request) );


class AddStandardView(View):
    form_class = AddStandardForm
    template_name = 'index/add_standard.html'

    def get(self, request):
        form = self.form_class()
        return render_to_response(self.template_name, {'form': form}, context_instance = RequestContext(request) );

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Seems Good")
        return render_to_response(self.template_name, {'form': form}, context_instance = RequestContext(request) );


class AddStudentView(AddStandardView):
    form_class = AddStudentForm
    template_name = 'index/add_student.html'


class AddTeacherView(AddStandardView):
    form_class = AddTeacherForm
    template_name = 'index/add_teacher.html'




