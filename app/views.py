from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect, get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponsePermanentRedirect

from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required

from app.models import AppUser


from .forms import UserForm



def IndexView(request):
    if request.user.is_anonymous:
        app_user = None

    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

    if request.method == "POST":
        pass

    else:

        context = {"app_user": app_user}
        return render(request, "app/index.html", context)



def SignInView(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)

                app_user = AppUser.objects.get(user__pk=request.user.id)
                
                if app_user.status == True:
                    return HttpResponseRedirect(reverse("app:index"))
                
                else:
                    messages.warning(request, "Sorry, validate your account")
                    return HttpResponseRedirect(reverse("app:sign_in"))
                
            else:
                context = {"message": "Sorry, Invalid Login Details"}
                return render(request, "app/error.html", context )


        else:
            context = {"message": "Sorry, Invalid Login Details"}
            return render(request, "app/error.html", context )

    else:
        context = {}
        return render(request, "app/sign_in.html", context )




def SignUpView(request):
    next = request.GET.get("next")
    if request.method == "POST":

        form = UserForm(request.POST or None, request.FILES or None)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        #password2 = request.POST.get("password2")
        name = request.POST.get("name")
        email = request.POST.get("email")



        if request.POST.get("password2") != request.POST.get("password1"):
            context = {"message": "Make sure both passwords match"}
            return render(request, "app/error.html", context )

            
        else:
            try:
                AppUser.objects.get(user__email=request.POST.get("username"))
                context = {"message": "Email Address already taken!"}
                return render(request, "app/error.html", context )


            except:
                user = form.save()
                user.set_password(request.POST.get("password1"))
                user.save()

                app_user = AppUser.objects.create(user=user)
                app_user.save()

                user = app_user.user
                user.email = email
                user.first_name = name
                user.last_name = name
                user.save()
                
                if user:
                    if user.is_active:
                        login(request, user)

                        if next:
                            return HttpResponsePermanentRedirect(next)
                        else:
                            return HttpResponseRedirect(reverse("app:sign_upf"))
                    

    else:
        form = UserForm()
        context = {"form": form}
        return render(request, "app/sign_up.html", context )


def SignUpFView(request):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        pass

    else:

        context = {"app_user": app_user}
        return render(request, "app/sign_upf.html", context)
    




def SignOutView(request):

    logout(request)
    return HttpResponseRedirect(reverse("app:sign_in"))
