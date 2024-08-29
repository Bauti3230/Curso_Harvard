from django.urls import path

from . import views

urlpatterns = [
	path("",views.index, name="index"),
	path("<str:name>", views.greet, name="greet"),
	path("bauti", views.bauti, name="bauti"),
	path("ale", views.ale, name="ale")
]