from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm, SignUpForm
from django.views.generic import View
from dropbox_user.models import DropBoxUser

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
            data = form.cleaned_data
            user = DropBoxUser.objects.create_user(
                    email = data["email"],
                    password = data["password"],
                    # confirm_password = data["confirm_password"],
                    username = data["username"]
            )
            # if password and confirm_password and password != confirm_password:
            #     raise forms.ValidationError('Passwords do not match')
            # return confirm_password
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("loginpage"))
