from django.urls import path
from . import views

<<<<<<< Updated upstream
urlpatterns = [
    path('', views.base, name='base'),
]
=======
urlpatterns=[
    path('', views.index, name='index'),
]
>>>>>>> Stashed changes
