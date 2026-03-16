from django.urls import path
from .views import create_employee,list_employee,delete_employee,update_employee

urlpatterns = [
    path('' , list_employee,name = "list"),
    path('create/',create_employee,name = "create"),
    path('update/<int:pk>/',update_employee,name = "update"),
    path('delete/<int:pk>/',delete_employee,name = "delete")
    
]