from django.shortcuts import render
from django.db import models
from .models import Users,Softwares,Downloads
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse,Http404
from django.conf import settings
import os
# Create your views here.

def index(request):
    s = Softwares.objects.all()
    return render(request, template_name='General/base_general.html',context={'soft_det':s})

def register(request):
    name = request.POST.get('name')
    username = request.POST.get('username')
    mail = request.POST.get('mail')
    mobile = request.POST.get('mobile')
    dob = request.POST.get('dob')
    password = request.POST.get('password')

    user = Users(name= name.strip(),username=username.strip(), mail=mail.strip(), mobile=mobile.strip(), dob=dob, password=password.strip())
    user.save()

    return redirect(log_pg)

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
          u = Users.objects.get(username=username.strip(), password=password.strip())
        except Users.DoesNotExist:
              return redirect(index)
        else:
          s = Softwares.objects.all()

          context = {'user_det': u, 'soft_det': s}
          return   render(request,template_name='General/softwares.html',context=  context)


def logout(request,user_id):
    return redirect(index)

def log_pg(request):
    return render(request,template_name='General/login.html')

def reg_pg(request):
    return render(request,template_name='General/register.html')

def G_softwares(request):
    if request.method == "POST":
        word = request.POST["search"]
        s = Softwares.objects.filter(name__contains =word )
        return render(request,template_name='General/base_general.html',context={'soft_det':s})
    else:
        s = Softwares.objects.all()
        return render(request,template_name='General/base_general.html',context={'soft_det':s})

def upload_pg(request,user_id):
    user = Users.objects.get(id= user_id)
    try:
        s = Softwares.objects.filter(own_by= user)
    except(Softwares.DoesNotExist):
        s = None;
        return render(request,template_name='General/upload.html', context= {'user_det': user,'soft_det':s})
    else:
        return render(request,template_name='General/upload.html', context= {'user_det': user,'soft_det':s})


def download_pg(request,user_id):
    user = Users.objects.get(id= user_id)
    down = Downloads.objects.filter(user=user)
    return render(request,template_name='General/download.html', context= {'user_det': user,'down_det':down})

def softwares_pg(request,user_id):
    user = Users.objects.get(id= user_id)
    if request.method == "POST":
        word = request.POST["search"]
        s = Softwares.objects.filter(name__contains= word )
        return render(request,template_name='General/softwares.html', context= {'user_det': user,'soft_det':s})
    else:
        s = Softwares.objects.all()
        return render(request,template_name='General/softwares.html', context= {'user_det': user,'soft_det':s})

def edit_pg(request,user_id):
    user = Users.objects.get(id= user_id)
    return render(request,template_name='General/edit.html', context= {'user_det': user})

def view_pg(request,user_id):
    user = Users.objects.get(id= user_id)
    return render(request,template_name='General/view.html', context= {'user_det': user})

def upload(request,user_id):
    if request.method == "POST":
        SoftwareName = request.POST["SoftwareName"]
        Descrpition = request.POST["Descrpition"]
        Requirements = request.POST["Requirements"]
        cover_pic = request.POST.get("pic_file",False)
        File = request.POST.get("file",False)
    user = Users.objects.get(id= user_id)
    soft = Softwares(own_by=user,name=SoftwareName.strip(),description=Descrpition.strip(),requirements=Requirements.strip(),cover_pic=cover_pic,zip_file=File)
    soft.save()
    s = Softwares.objects.all()
    return render(request,template_name='General/softwares.html', context= {'user_det': user,'soft_det':s})

def soft_view(request,user_id,soft_id):
    user = Users.objects.get(id= user_id)
    soft = Softwares.objects.get(id=soft_id)
    return render(request,template_name='General/soft_view.html', context= {'user_det': user,'soft_det':soft})


def G_softwares_view(request,soft_id):
    soft = Softwares.objects.get(id=soft_id)

    return render(request,template_name='General/g_view.html', context= {'soft_det':soft})

def g_down(request,soft_id):
    soft = Softwares.objects.get(id=soft_id)
    file_path = os.path.join(settings.MEDIA_ROOT,str(soft.zip_file))
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            soft.download = soft.download+1
            soft.save()
            return response
    else:
        raise Http404

def down(request,user_id,soft_id):
    user = Users.objects.get(id=user_id)
    soft = Softwares.objects.get(id=soft_id)
    try:
        d = Downloads.objects.get(user=user,soft=soft)
    except(Downloads.DoesNotExist):
        d=None
    file_path = os.path.join(settings.MEDIA_ROOT,str(soft.zip_file))
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            if d is  None:
                down = Downloads(user= user,soft=soft)
                down.save()
            soft.download = soft.download+1
            soft.save()

            return response
    else:
        raise Http404
