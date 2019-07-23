from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User

from .models import Menu, Item, Ingredient
from .forms import MenuForm

# Run tests with "python manage.py test"

menu_data1 = {
    'season': 'Summer',
    'expiration_date': '2020-03-20'
}

menu_data2 = {
    'season': 'Winter',
    'expiration_date': '2020-06-20'
}

class MenuViewsTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            username='test_user',
            email='testemail@gmail.com',
            password='testing'
        )
        ingredient1 = Ingredient(name='chocolate')
        ingredient1.save()
        ingredient2 = Ingredient(name='strawberry')
        ingredient2.save()
        ingredient3 = Ingredient(name='banana')
        ingredient3.save()
        self.item1 = Item(
            name='Item 1',
            description='testing items',
            chef=self.test_user
        )
        self.item1.save()
        self.item1.ingredients.add(ingredient1, ingredient2)
        self.menu1 = Menu.objects.create(**menu_data1)
        self.menu1.items.add(self.item1)
        self.menu2 = Menu.objects.create(**menu_data2)
        self.menu2.items.add(self.item1)

    def tearDown(self):
        self.test_user.delete()
        
    def test_menu_list_view(self):
        resp = self.client.get(reverse('menu_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.menu1, resp.context['menus'])
        self.assertIn(self.menu2, resp.context['menus'])
        self.assertTemplateUsed(resp, 'menu/list_all_current_menus.html')
        self.assertContains(resp, self.menu1.season)
        
    def test_menu_detail_view(self):
        resp = self.client.get(reverse('menu_detail',
            kwargs={'pk': self.menu1.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.menu1, resp.context['menu'])
        self.assertTemplateUsed(resp, 'menu/menu_detail.html')
        
    def test_edit_menu_view_GET(self):
        resp = self.client.get(reverse('menu_edit',
            kwargs={'pk': self.menu1.pk}))
        self.assertEqual(resp.status_code, 200)

class MenuModelTest(TestCase):
    def test_menu_creation(self):
        menu = Menu.objects.create(**menu_data1)
        self.assertEqual(menu.season, 'Summer')



    
