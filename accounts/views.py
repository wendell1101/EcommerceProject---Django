from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth import authenticate, login, logout



from .forms import RegisterForm, LoginForm

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request,f'An account has been created for {email}. Login now!')
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/register.html',context)
    # success_message = f'An account for {email} has been created.'


class LoginView(LoginView):
    template_name = 'accounts/login.html'

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request,'You have been logged out. Login again')
        return redirect('accounts:login')
    return render(request,'accounts/logout.html')
    
