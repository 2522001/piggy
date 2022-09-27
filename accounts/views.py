from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model

User = get_user_model()


# 회원 가입
def signup(request):
    if request.method == 'POST':
        # print("keyword1", request.POST.get('keyword1'))
        # print("keyword2", request.POST.get('keyword2'))
        user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password'],
                                        email=request.POST['email'],
                                        keyword1=request.POST['keyword1'],
                                        keyword2=request.POST['keyword2'])
        auth.login(request, user)
        print("POST 요청 날아감")
        return redirect('/')
    else:
        print("GET 요청 날아감.")
        return render(request, 'signup.html')


# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)

        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'login.html', {'error': 'email or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'login.html')


# 로그 아웃
def logout(request):
    auth.logout(request)
    return redirect('/')