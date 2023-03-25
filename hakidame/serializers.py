from rest_framework import serializers
from .models import Hakidame


class HakidameSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Hakidame
        fields = '__all__'

    def create(self, validated_data):
        newHakidame = Hakidame.objects.create(
            title=validated_data["title"],
            detail=validated_data["detail"],
            todo=validated_data["todo"],
            done=validated_data["done"],
            bookmark=validated_data["bookmark"]
        )
        newHakidame.save()
        return newHakidame

    def update(self, instance, validated_data):
        instance.title = validated_data["title"]
        instance.detail = validated_data["detail"]
        instance.todo = validated_data["todo"]
        instance.done = validated_data["done"]
        instance.bookmark = validated_data["bookmark"]
        instance.save()

        return instance

    def delete(self):
        self.delete(is_hard=True)
