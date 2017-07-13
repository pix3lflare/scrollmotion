from models import Image, CompressedImageOne, CompressedImageTwo
from rest_framework import serializers


class CompressedImageOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompressedImageOne
        fields = '__all__'


class CompressedImageTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompressedImageTwo
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    compressed_one = CompressedImageOneSerializer()
    compressed_two = CompressedImageTwoSerializer()

    class Meta:
        model = Image
        fields = ('id', 'image_url', 'name', 'size', 'compressed_one', 'compressed_two')

    def get_image_url(self, obj):
        return obj.image.url

    def get_name(self, obj):
        return obj.image.name.split('/')[-1]

    def get_size(self, obj):
        return obj.image.size


