from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
# auth가 특정 개체가 있는지 없는지 판단해주는 역할 중요!!!!!!
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserChangeForm



def login(request):
    # POST 요청이 들어오면 로그인 처리를 해준다
    if request.method == 'POST':
    # GET 요청이 들어오면 login form을 담고 있는 login.html을 띄워준다
        userid= request.POST['username']
        pwd= request.POST['password']
        # 사용자가 입력한 id pw를 파이썬 변수에 담아두고
        # 밑줄의 경우 실제 데베에 있는지 확인하는 역할
        user = auth.authenticate(request, username=userid,password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

@csrf_exempt
def create_account(request):
    if request.method == "POST":
        if request.POST.get('password') == request.POST.get('repeat'):
            #회원가입   
            new_user = User.objects.create_user(username=request.POST.get('username'),password = request.POST.get('password'), first_name=request.POST.get('first_name'), email=request.POST.get('email'))
            new_user.save() 
            #로그인
            auth.login(request, new_user)
            #홈 리다이렉션 
            return render(request, 'index.html')
    return render(request, 'accounts/create_account.html')

