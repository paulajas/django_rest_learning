from datetime import datetime
from django.test import TestCase
from receipe.models import MeatReceipe

class TestMeatReceipeCase(TestCase):
    def setUp(self):
        MeatReceipe.objects.create(meat_kind="leg", meat_type="red", name="roasted meat", make_time=30, hard_level="easy", kcal=150, alergens=['protein', 'lactose'], for_children=True, make_date=datetime.now().date()).save()

    def testName1(self):
        self.assertEqual(5+9, 14)

class AnimalTestCase(TestCase):
    def setUp(self):
        print("Good")