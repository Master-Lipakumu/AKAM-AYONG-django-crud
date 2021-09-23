
from django.urls import path

from .views import index, Maladeform, maladelist, delete, MaladeUpdate, search

app_name ='malade'

urlpatterns = [
    path('', index, name="index"),
    path('search/',search, name="search"),
    path('maladeform/', Maladeform.as_view(), name="maladeform"),
    path('maladeview/', maladelist, name='maladeview'),
    path('maladeview/update/<int:pk>', MaladeUpdate.as_view(), name="update"),
    path('maladeview/delete/<int:id>', delete, name="delete"),
]
