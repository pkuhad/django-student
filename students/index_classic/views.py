import logging

from django.conf import settings
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from students.index_classic.forms import *

def index(request):
    '''
    Handles the index request of application. When logged in it redirects to /home
    '''
    return render_to_response('index/index.html', context_instance = RequestContext(request) );

def add_standard(request):
    form = AddStandardForm()
    if request.method == "POST":
        form = AddStandardForm(request.POST)
        if form.is_valid():
            return HttpResponse("Seems Good")
     
    context = {
            'form': form
    }
    return render_to_response('index/add_standard.html', context, context_instance = RequestContext(request) );

def add_student(request):
    return render_to_response('index/add_student.html', context_instance = RequestContext(request) );



