from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView
from .models import User
from .models import Class_number
from django.contrib import messages

from .forms import SignupForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
# Create your views here.


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'signup.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('profile')

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('profile')
        return super(SignupView, self).get(*args,**kwargs)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'GET':
            return render(request,'login.html')
        elif request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username =username,password=password)
            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
                print('Wrong username OR password')
                return redirect('login')





def logout_user(request):
    logout(request)
    return redirect('login')


#With ListView of all classes
#@login_required(login_url='login')
#def profile(request):
#    return render(request,'profile.html')

@method_decorator(login_required(login_url='login'),name="dispatch")
class ProfileView(ListView):
    model = Class_number
    template_name = 'profile.html'

    def post(self, request, *args, **kwargs):
        return render(request, 'done.html')


    def done(self):
        return render(self,'done.html')

    def donee(self):
        return render(self,'donee.html')


    def back_home(self):
        return render(self,'profile.html')


@method_decorator(login_required(login_url='login'),name="dispatch")
class AccountSettingsView(UpdateView):
    model = User
    fields = ['first_name','last_name','school_type','class_number']
    template_name = 'account_settings.html'
    success_url = '/profile/'
    def get_object(self, queryset=None):
        return self.request.user

