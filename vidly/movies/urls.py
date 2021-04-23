from django.urls import path
from .import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:movie_Id>', views.details, name='movie_details')
]