from django.urls import path
from . import views  # from the current directory import the views module

# movies/
# movies/1/details


# url configuration

app_name = 'movies'  # use that instead of typing 'movies_index' below

urlpatterns = [
    # passing a reference to views/index, not calling the funciton
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')

]
