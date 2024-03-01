from rest_framework import serializers
from .models import MenuItem, BookingItem

class MenuItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']
        
        
        
class BookingItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BookingItem
        fields = '__all__'
        