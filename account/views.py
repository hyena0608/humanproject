from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import CustomUser
from .models import Hobby
from django.forms.models import model_to_dict
# Create your views here.

def login_view(request):
    # AuthenticationForm: 장고에서 제공하는 로그인 기능 폼
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid(): # 데이터가 유효하다면 
            # cleand_date: 검증에 통과한 값을 사전타입으로 만들어준다.
            username = form.cleaned_data.get("username") 
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None: # user 데이터가 존재한다면
                login(request, user)
            return redirect("main")
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main')
  

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("main")
    else:    
        form = RegisterForm()
        return render(request, 'signup.html', {'form':form})


        

def mypage(request):    
    Hobbys = Hobby.objects.all()
    return render(request, 'mypage.html', {'Hobbys': Hobbys})
