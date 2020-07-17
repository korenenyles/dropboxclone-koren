from django.contrib import messages
from dropbox_user.models import DropBoxUser
from django.views.generic import View
from authentication.forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


__author__ = ["mprrodhan",
            "https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html",
            "mailkMAlna",
            "peter marsh"]


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "general_form.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                email=data["email"],
                                password=data["password"]
                                )
            if user:
                login(request, user)
                return HttpResponseRedirect(request
                                            .GET.get('next',
                                                     reverse("landingpage")))
        
class LogoutView(View):
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("loginpage"))


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "general_form.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            user = authenticate(
                email,
                password=password,
                username=username
            )
            if user:
                login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('loginpage'))
            )
        else:
            return render(request, "general_form.html", {"form": form})
