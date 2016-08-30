#!/usr/bin/env python
# -*- coding:utf-8 -*-  


from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime


def hello(request):
    return HttpResponse('hello')

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body> It is now %s.</body></html>'%now
    return HttpResponse(html)

def hours_ahead(request):
    current_datetime = datetime.datetime.now()
    '''
    t=get_template('current_datetime.html')
    html = t.render(Context({'current_date':now})) 
    return HttpResponse(html)
    '''
    return render_to_response('current_datetime.html',locals())


    
