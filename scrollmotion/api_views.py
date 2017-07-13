from models import Image
from serializers import ImageSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route


# Images - API Views
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request):
        data = request.data
        print 'IMAGe DATA: '
        print data
        data['user'] = self.request.user.id
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def list(self, request):
        images = Image.objects.filter(user=self.request.user).select_related('compressed_one', 'compressed_two')
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
