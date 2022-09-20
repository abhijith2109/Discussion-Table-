#serializer --> It take python objects turn into a json object or a javascript object , then we can return that

from rest_framework.serializers import ModelSerializer
from base.models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

