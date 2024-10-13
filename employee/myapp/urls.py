from django.urls import path
from myapp import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
   path('signup/',views.SignupView.as_view()),
   path('employee/add/',views.EmployeeCreateView.as_view()),
   path('employee/<int:pk>/',views.EmployeeRUDView.as_view()),
   path('token/',ObtainAuthToken.as_view())
]