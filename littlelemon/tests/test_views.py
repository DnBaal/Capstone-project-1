from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        
        self.url = reverse('menu-items')
        
        self.menuitem1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.menuitem2 = MenuItem.objects.create(title="SaladCesar", price=60, inventory=80)

    
    
    def test_getall(self):

        response = self.client.get(self.url)

        menu_items = MenuItem.objects.all()
        menuitem_serializer = MenuItemSerializer(menu_items, many=True)
        serialized_data = menuitem_serializer.data
        
        self.assertEqual(serialized_data, response.data)