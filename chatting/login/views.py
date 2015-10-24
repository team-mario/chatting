from django.shortcuts import render
from .form import RegisterForm
from django.http import HttpResponseRedirect
from .models import User


def index(request):
    form = RegisterForm
    return render(request, 'login/main.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        user_id = request.POST.get('name')
        password1 = request.POST.get('password')
        password2 = request.POST.get('checkPassword')

        name_list = User.objects.filter(name=user_id).order_by('name')
        isvalid = True
        for list in name_list:
            isvalid = False

        if form.is_valid() and password1 == password2 and isvalid == True:
            save_user_information(user_id, password1)
            return HttpResponseRedirect('/')
        else:
            form = RegisterForm
            return render(request, 'login/main.html', {'msg': 'Invalid id or password', 'form': form})


def login(request):
    if request.method == 'POST':
        input_name = request.POST.get('login-id')
        input_password = request.POST.get('login-password')
        name_list = User.objects.filter(name=input_name).order_by('id')

        saved_name = None

        for list in name_list:
            saved_name = list.name
            password = list.password

        if saved_name is not None and input_password == password:
            context = {'name_list': name_list, 'login_id': input_name}
            print('OK')
            return render(request, 'message/list.html', context)
        else:
            form = RegisterForm
            return render(request, 'login/main.html', {'msg': 'Invalid id or password', 'form': form})


def save_user_information(aname, apassword):
    q = User(name=aname, password=apassword)
    q.save()

