from models import Image, CompressedImageOne, CompressedImageTwo
from rest_framework import serializers


class CompressedImageOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompressedImageOne
        fields = ('id', 'url', 'name', 'size', 'quality')


class CompressedImageTwoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompressedImageTwo
        fields = ('id', 'url', 'name', 'size', 'quality')


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(required=False)
    name = serializers.SerializerMethodField(required=False)
    size = serializers.SerializerMethodField(required=False)
    quality = serializers.SerializerMethodField(required=False)
    compressed_one = CompressedImageOneSerializer(required=False)
    compressed_two = CompressedImageTwoSerializer(required=False)

    class Meta:
        model = Image
        fields = ('id', 'user', 'image', 'url', 'name', 'size', 'quality', 'compressed_one', 'compressed_two')

    def get_url(self, obj):
        return obj.image.url

    def get_name(self, obj):
        return obj.image.name.split('/')[-1]

    def get_size(self, obj):
        return obj.image.size

    def get_quality(self, obj):
        return 100

