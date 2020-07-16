from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm, SignUpForm
from django.views.generic import View
from dropbox_user.models import DropBoxUser

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
                return HttpResponseRedirect(request.GET.get('next', reverse("landingpage")))

class LogoutView(View):
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
            register = authenticate(
                email,
                password=password,
                username=username
            )
            login(request, register)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('loginpage'))
            )
        else:
            return render(request, "general_form.html", {"form": form})

# class SignUpView(View):
#     def get(self, request):
#         form = SignUpForm()
#         return render(request, "general_form.html", {"form": form})

#     def post(self, request):
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             if data['password1'] != data['password2']:
#                 return HttpResponse("Please enter a password!")
#             user = DropBoxUser.objects.create_user(
#                     email = data["email"],
#                     password = data["password1"],
#                     # password2 = data["password2"],
#                     username = data["username"]
#             )
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse("loginpage"))
