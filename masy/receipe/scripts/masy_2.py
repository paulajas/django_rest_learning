import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "masy.settings")

from datetime import datetime
from receipe.models import CookBook, CookBookReceipe, Country, Picture, Tag
from receipe.models import MeatReceipe

def run(*args):
    
    # MeatReceipe.objects.create(meat_kind="leg", meat_type="red", name="roasted meat", make_time=30, hard_level="easy", kcal=150, alergens=['protein', 'lactose'], for_children=True, make_date=datetime.now().date()).save()
    Country.objects.create(name="Szwecja").save()
    Tag.objects.create(name="test-tag").save()
    CookBook.objects.create(name="Test").save()
    Picture.objects.create(image_no="22").save()
    MeatReceipe.objects.create(
        meat_kind="leg",
        meat_type="red",
        name="roasted meat",
        make_time=30,
        hard_level="easy",
        kcal=150,
        alergens=['protein', 'lactose'],
        for_children=True,
        make_date=datetime.now().date(),
        country=Country.objects.get(pk=1)
        )
    obj = MeatReceipe.objects.get(pk=1)
    obj.tag.add(Tag.objects.get(pk=1)) # połączenie Tag z MeatReceipe => jeden do wielu
    obj.save()
    print(f"After adding tag: {MeatReceipe.objects.get(pk=1).tag.all()[0].name}")
    CookBookReceipe.objects.create(receipe=MeatReceipe.objects.get(pk=1), cookbook=CookBook.objects.get(pk=1), ratio=1) # asocjacja z atrybutem
    print(f"CookBookReceipe as association with attribute: {CookBookReceipe.objects.get(receipe=MeatReceipe.objects.get(pk=1), cookbook=CookBook.objects.get(pk=1), ratio=1)}")
    MeatReceipe.objects.filter(pk=1).update(picture= Picture.objects.get(pk=1)) # asocjacja kwalifikowana
    print(f"Picture added as qualified association: {MeatReceipe.objects.get(pk=1).picture} ")
    print(f"Picture also can show receipe: {Picture.objects.get(pk=1).receipe_set.all()}")
    country_test = Country(name="Test_new")
    try:
        MeatReceipe.objects.create(
            meat_kind="leg",
            meat_type="red",
            name="roasted meat",
            make_time=30,
            hard_level="easy",
            kcal=150,
            alergens=['protein', 'lactose'],
            for_children=True,
            make_date=datetime.now().date(),
            country=country_test
            ) # nie zapisze się bo kompozycja źródło: https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/
    except:
        print("Composition error")
    print("And on the end: delete Country id = 1")
    Country.objects.get(pk=1).delete()
    try:
        MeatReceipe.objects.get(pk=1)
    except:
        print("There is no receipe")

