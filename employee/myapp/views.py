from django.shortcuts import render


# Create your views here.
from rest_framework import generics,authentication,permissions
from myapp.serializers import UserCreateSerializer,EmployeeSerializer
from myapp.models import Employee


class SignupView(generics.CreateAPIView):
    serializer_class=UserCreateSerializer


class EmployeeCreateView(generics.CreateAPIView):
    serializer_class=EmployeeSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self,serializer):

        return serializer.save(user_object=self.request.user)
    
class EmployeeRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        qs=Employee.objects.filter(user_object=self.request.user)
        return qs
    
    