from rest_framework import serializers

from core.models import CheckList, CheckListItem


#  if we just used serializer then manuallly we have to define serializers fields in our serializers.py file...

# class CheckListSerializer(serializers.Serializer):
#     # title = serializers.CharField()
#     # is_deleted = serializers.BooleanField()
#     # is_archived = serializers.BooleanField()
#     # created_on = serializers.DateTimeField()
#     # modified_on = serializers.DateTimeField()


class CheckListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckListItem
        fields = '__all__'

class CheckListSerializer(serializers.ModelSerializer):
    items = CheckListItemSerializer(source='checklistitem_set',many=True)
    class Meta:
        model = CheckList
        fields = "__all__"


