import logging

from django.conf import settings
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt


def index(request):
    '''
    Handles the index request of application. When logged in it redirects to /home
    '''
    return render_to_response('index/index.html', context_instance = RequestContext(request) );

def add_student(request):
    return render_to_response('index/add_student.html', context_instance = RequestContext(request) );



