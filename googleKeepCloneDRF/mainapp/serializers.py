
from rest_framework import serializers
from mainapp.models import CheckList,CheckListItem

class AllListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = "__all__"
        
        
class CheckListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckListItem
        fields = "__all__"