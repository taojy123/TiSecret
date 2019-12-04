import datetime
import os
import re
import urllib.parse

from django.conf import settings
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render


REPORT_DIR_MAP = {
    '借呗': 'jiebei_report',
    '账管平台': 'zgpt_report',
    '串串钱包': 'ccqb_report',
}


def redirect(request):
    return HttpResponseRedirect('/store/documents/')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            msg = u'用户名或密码错误!'
            
    if not User.objects.exists():
        u = User.objects.create(username='admin', is_staff=True, is_superuser=True)
        u.set_password('tiadmin')
        u.save()
        
    return render(request, 'store/login.html', locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
    

@login_required(login_url='/store/login/')
def documents(request):
    user = request.user
    return render(request, 'store/documents.html', locals())


@login_required(login_url='/store/login/')
def api_documents(request):

    user = request.user
    docs = user.document_set.all().order_by('-updated_at')
    
    rs = []
    for doc in docs:
        rs.append(doc.to_dict())
    
    return JsonResponse({'rs': []})

