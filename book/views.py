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
from book.models import Book



@login_required(login_url="/sign-in/")
def AddView(request):
    if request.user.is_anonymous:
        app_user = None

    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        year = request.POST.get("year")

        book = Book.objects.create(app_user=app_user, title=title, author=author, year=year)
        book.save()

        return HttpResponseRedirect(reverse("book:add"))

    else:
        books = Book.objects.filter(app_user=app_user).order_by('-pub_date')
        context = {"app_user": app_user, "books": books}
        return render(request, "book/add.html", context)


def EditView(request, book_id):
    if request.user.is_anonymous:
        app_user = None

    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        year = request.POST.get("year")

        book = Book.objects.get(id=book_id)
        book.title = title
        book.author = author
        book.year = year
        book.save()

        return HttpResponseRedirect(reverse("book:add"))

    else:
        book = Book.objects.get(id=book_id)
        
        context = {"app_user": app_user, "book": book}
        return render(request, "book/edit.html", context)


def RemoveView(request, book_id):
    if request.user.is_anonymous:
        app_user = None

    else:
        app_user = AppUser.objects.get(user__pk=request.user.id)

    if app_user:
        book = Book.objects.get(id=book_id)
        book.delete()

        return HttpResponseRedirect(reverse("book:add"))


