from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def userlogin(request):
    if request.method == 'POST':
        strUserName = request.POST.get('username')
        strPassword = request.POST.get('password')


        user = authenticate(username=strUserName,password=strPassword)
        if user is not None:
            login(request,user)
            return redirect('post')
        else:
            messages.error(request,'invalid username or password')
    return render(request,'login.html')

def registration(request):
    if request.method == 'POST':
        strUserName = request.POST.get('username')
        strFirstName = request.POST.get('firstname')
        strLastName = request.POST.get('lastname')
        strEmail =request.POST.get('email')
        strPassword1 = request.POST.get('password1')
        strPassword2 = request.POST.get('password2')

        if strUserName and strPassword1 and strPassword2:
            if strPassword1 == strPassword2 :
                user = User.objects.filter(username=strUserName)
                if not user:
                    user = User.objects.create_user(
                        username = strUserName,
                        first_name = strFirstName,
                        last_name = strLastName,
                        email = strEmail,
                        password = strPassword2
                    )
                    messages.success(request,'Registration successful!!')
                    return redirect('login')
                else:
                    messages.error(request,'username already exist')
            else:
                messages.error(request,'Password do not match!!')
        else:
            messages.error(request,'form fill properly!!')

    return render(request,'registration.html')


def userLogout(request):
    logout(request)
    return redirect('login')