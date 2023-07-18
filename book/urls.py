from django.urls import path
from . import views

app_name = "book"

urlpatterns = [

	path("add/", views.AddView, name="add"),
    path("edit/<int:book_id>/", views.EditView, name="edit"),
    path("remove/<int:book_id>/", views.RemoveView, name="remove"),
    #path("detail/", views.DetailView, name="detail"),

]