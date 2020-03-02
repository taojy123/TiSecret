import datetime
import os
import re
import urllib.parse

from django.conf import settings
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404

from store.models import Document, Chip

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
    

@login_required
def documents(request):
    user = request.user
    menu = request.GET.get('menu', 'documents')
    code = request.GET.get('code')
    CODE_MAP = {
        'a': '请输入名称',
        'b': '只接受加密后的数据',
        'c': '成功加密保存',
    }
    msg = CODE_MAP.get(code, '')
    return render(request, 'store/documents.html', locals())
    

@login_required
def new_document(request):
    user = request.user
    name = request.POST.get('name', '')
    content = request.POST.get('content', '')
    if not name:
        return HttpResponseRedirect('/store/documents/?menu=new&code=a')
    if not content.startswith('@@'):
        return HttpResponseRedirect('/store/documents/?menu=new&code=b')
    Document.objects.create(user=user, name=name, content=content)
    return HttpResponseRedirect('/store/documents/?code=c')
    

@login_required
def update_document(request):
    user = request.user
    id = request.POST.get('id')
    content = request.POST.get('content', '')
    doc = get_object_or_404(user.document_set, id=id)
    if not content.startswith('@@'):
        return HttpResponseRedirect('/store/documents/?menu=view&code=b')
    doc.content = content
    doc.save()
    return HttpResponseRedirect('/store/documents/?code=c')
    

def chip(request, chip_token):
    menu = 'crypt'
    return render(request, 'store/documents.html', locals())


@login_required
def api_documents(request):
    user = request.user
    docs = user.document_set.all().order_by('-updated_at')
    rs = []
    for doc in docs:
        r = doc.to_dict()
        del r['user']
        del r['content']
        rs.append(r)
    return JsonResponse({'rs': rs})


@login_required
def api_document(request, document_id):
    user = request.user
    doc = user.document_set.filter(id=document_id).first()
    if doc:
        r = doc.to_dict()
        del r['user']
        return JsonResponse(r)
    return HttpResponseNotFound()


def api_chip(request):
    if request.method == 'GET':
        token = request.GET.get('token')
        chip = get_object_or_404(Chip, token=token)
        return JsonResponse(chip.to_dict())

    token = request.POST.get('token')
    content = request.POST.get('content')
    if not content.startswith('@@'):
        return HttpResponseBadRequest('请先加密后保存')
    
    chip, created = Chip.objects.get_or_create(token=token)
    chip.content = content
    chip.save()
    return JsonResponse(chip.to_dict())
    

