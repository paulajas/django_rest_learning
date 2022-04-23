from datetime import datetime
from django.test import TestCase
from receipe.models import MeatReceipe

class MeatReceipeTestCase(TestCase):
    def setUp(self):
        MeatReceipe.objects.create(meat_kind="leg", meat_type="red", name="roasted meat", make_time=30, hard_level="easy", kcal=150, alergens=['protein', 'lactose'], for_children=True, make_date=datetime.now().date()).save()
