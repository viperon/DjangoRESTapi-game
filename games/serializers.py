from rest_framework import serializers
from games.models import Game


class GameSerializer(serializers.Serializer):
    class Meta:
        model = Game
        fields = (
            'id',
            'name',
            'release_date',
            'game_category',
            'played',
        )
    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.game_category = validated_data.get('game_category', instance.game_category)
        instance.played = validated_data.get('played', instance.played)
        instance.save()
        return instance

