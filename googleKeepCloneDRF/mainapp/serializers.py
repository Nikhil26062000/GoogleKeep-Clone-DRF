
from rest_framework import serializers
from mainapp.models import CheckList

class AllListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = "__all__"