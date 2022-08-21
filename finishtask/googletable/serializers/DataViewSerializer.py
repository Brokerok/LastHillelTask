from rest_framework import serializers
from googletable.models.data import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = "__all__"
