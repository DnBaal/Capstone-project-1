from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem, BookingItem
from .serializers import MenuItemSerializer, BookingItemSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingItem.objects.all()
    serializer_class = BookingItemSerializer
    permission_classes = [IsAuthenticated]
    
    
    
