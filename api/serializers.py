from rest_framework import serializers

from api.models import Picture, Category


class PictureSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True, allow_empty_file=False)
    class Meta:
        model = Picture
        fields = ('image', 'caption', "category")


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True, allow_empty_file=False)
    class Meta:
        model = Category
        fields = ('name','image')


class CategoryPicturesSerializer(serializers.ModelSerializer):
    pictures = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ("name", 'image',"pictures")