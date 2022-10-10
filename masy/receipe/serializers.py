from .models import City, Country, Picture, TagCountry
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):

    len_name = serializers.SerializerMethodField()

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=30)

    class Meta:
        model = Country
        fields = "__all__"

    def get_len_name(self, object):
        length = len(object.name)
        return length

    def create(self, validated_data):
        return Country.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is to short!")
        else:
            return value

    def validate(self, data):
        if Country.objects.get(name=data["name"]):
            raise serializers.ValidationError("This country already exists!")
        else:
            return data


class CitySerializer(serializers.ModelSerializer):
    country = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='country-list')
    class Meta:
        model=City
        fields = "__all__"


class PictureSerializer(serializers.Serializer):

    def image_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Number is too short!")

    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField()
    image_no=serializers.CharField(validators=[image_name])

    def create(self, validated_data):
        return Picture.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.image = validated_data.get("image", instance.image)
        instance.image_no = validated_data.get("image_no", instance.image_no)
        instance.save()
        return instance

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id', 'tag_text')
        abstract=True

class TagCountrySerializer(TagSerializer):
    # country = CountrySerializer(read_only=True)
    # country = serializers.StringRelatedField()
    # country = serializers.PrimaryKeyRelatedField(read_only=True)
    country = serializers.HyperlinkedRelatedField(
        lookup_field ='',
        read_only=True,
        view_name='country-list')
    class Meta:
        model=TagCountry
        fields = TagSerializer.Meta.fields + ("name_in_country_language", "name_in_english", "country")


