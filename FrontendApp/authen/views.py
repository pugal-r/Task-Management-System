from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        pasw=request.POST['pasw']

        try:
            u=User.objects.get(username=uname)
            return render(request,"register.html",{'error':True})
        except:

            u=User.objects.create_user(
                first_name=fname,
                last_name=lname,
                username=uname,
                email=email,
                password=pasw
            )
            print(u)
            print(User.objects.all())
            return redirect(login_)

    return render(request,"register.html")

def login_(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        pasw=request.POST['pasw']
        auth=authenticate(username=uname,password=pasw)

        if auth:
            login(request,auth)
            messages.success(request,'Login Completed..!')
            return redirect('home')
        else:
            messages.error(request,"Wrong Crenditials Check")
            return redirect(login_)
    return render(request,"login_.html")

def logout_(request):
    logout(request)
    messages.success(request,"Logout Succussfully..!")
    return redirect(login_)

def profile(request):
    return render(request,"profile.html")

def updatep(request):
    data=request.user
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']

        data.first_name=fname
        data.last_name=lname
        data.username=uname
        data.email=email
        data.save()
        return redirect(profile)
    return render(request,"updatep.html",{'data':data})

def reset_pasw(request):
    data=User.objects.get(username=request.user)

    if 'old_pasw' in request.POST:
        old_pasw=request.POST['old_pasw']
        a=authenticate(username=data.username,password=old_pasw)

        if a:
            messages.success(request,"Password RESET Succussfully..!")
            return render(request,"reset_pasw.html",{'new':True})
        else:
            messages.error(request,"Old Password Is Wrong..!")
            return redirect(reset_pasw)
    
    if 'new_pasw' in request.POST:
        new_pasw=request.POST['new_pasw']
        if data.check_password(new_pasw):
            messages.error(request,'Enter a Different Password')
            return redirect(reset_pasw)
        data.set_password(new_pasw)
        data.save()
        return redirect(login_)
    
    return render(request,"reset_pasw.html")

def forget_pasw(request):

    if request.method == 'POST':
        if 'uname' in request.POST:
            uname=request.POST['uname']
            try:
                user=User.objects.get(username=uname)
                request.session['fp_user'] = user.username
                return render(request,"forget_pasw.html",{'new':True})
            except:
                messages.error(request,'Username Does not Exist')
                return redirect(forget_pasw)
        
        if 'new_pasw' in request.POST:
            user=request.session.get('fp_user')
            data=User.objects.get(username=user)
            new_pasw=request.POST['new_pasw']

            if data.check_password(new_pasw):
                messages.error(request,'Enter a Different Password')
                return redirect(forget_pasw)
            
            data.set_password(new_pasw)
            data.save()
            del request.session['fp_user']
            return redirect(login_)
    return render(request,"forget_pasw.html")