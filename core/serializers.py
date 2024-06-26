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
        fields = "__all__"


class CheckListSerializer(serializers.ModelSerializer):
    items = CheckListItemSerializer(many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CheckList
        fields = "__all__"

    def create(self, validated_data):

        validated_data.pop("user", None)
        user = self.context["request"].user
        checklist = CheckList.objects.create(user=user, **validated_data)
        return checklist
