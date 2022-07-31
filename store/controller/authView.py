from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User

from store.forms import CustomUserForm


def register(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, "Registered Successfully! Login to Continue")
            return redirect("login")
    data = {
        "form": form
    }
    return render(request, "store/auth/register.html", data)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = auth.authenticate(request,username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You are loggged in")
                return redirect("home")
            else:
                messages.error(request, "Invalid User Credentials")
                return redirect("login")
        return render(request, "store/auth/login.html")


def logoutpage(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, "Logout Succussfully")
        return redirect("home")
    return redirect("home")

