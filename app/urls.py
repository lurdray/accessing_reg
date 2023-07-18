from django.urls import path
from . import views

app_name = "app"

urlpatterns = [

	path("sign-in/", views.SignInView, name="sign_in"),
	path("sign-up/", views.SignUpView, name="sign_up"),
    path("sign-up/finish/", views.SignUpFView, name="sign_upf"),
    path("sign-out/", views.SignOutView, name="sign_out"),
    path("app/", views.IndexView, name="index"),

]