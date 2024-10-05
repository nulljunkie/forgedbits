from rest_framework import generics, mixins, permissions
from rest_framework.serializers import ValidationError

from .models import Item
from .serializers import ItemSerializer


class ItemAPIView(mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):


    permission_classes = [permissions.AllowAny]

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        if Item.objects.filter(name=serializer.validated_data['name']).exists():
            raise ValidationError("Item with this name already exists.")
        serializer.save()

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

