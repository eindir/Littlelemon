from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import Menu, Booking
from django.contrib.auth.models import User
from .serializer import MenuSerializer, BookingSerializer, UserSerializer

# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
def index(request):
    return render(request, 'index.html', {})
