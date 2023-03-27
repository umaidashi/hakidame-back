
from rest_framework import generics
from rest_framework.parsers import JSONParser
from .serializers import HakidameSerializer, TagSerializer
from .models import Hakidame,Tag


class HakidameView(generics.ListCreateAPIView):
    queryset = Hakidame.objects.order_by('-pub_date')
    serializer_class = HakidameSerializer


class HakidameTodoView(generics.ListCreateAPIView):
    parser_classes = [JSONParser]
    queryset = Hakidame.objects.order_by('-pub_date').filter(todo=True)
    serializer_class = HakidameSerializer

class HakidameBookmarkView(generics.ListCreateAPIView):
    queryset = Hakidame.objects.order_by('-pub_date').filter(bookmark=True)
    serializer_class = HakidameSerializer


class HakidameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hakidame.objects.all()
    serializer_class = HakidameSerializer

class TagsView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer