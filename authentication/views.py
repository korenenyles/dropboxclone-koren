from dropbox_user.models import DropBoxUser
from django.views.generic import View
from authentication.forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
            data = form.cleaned_data
            if data['password1'] != data['password2']:
                return HttpResponse("Please enter a password!")
            user = DropBoxUser.objects.create_user(
                email=data["email"],
                password=data["password1"],
                # password2 = data["password2"],
                username=data["username"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("loginpage"))
