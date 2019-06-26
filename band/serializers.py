from rest_framework import serializers
from band.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name')
    # first_name = serializers.CharField(
    #     required=False, allow_blank=True, max_length=100)
    # last_name = serializers.CharField(
    #     required=False, allow_blank=True, max_length=100)

    # def create(self, validated_data):
    #     return Person.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.first_name = validated_data.get(
    #         'first_name', instance.first_name)
    #     instance.last_name = validated_data.get(
    #         'last_name', instance.last_name)
    #     instance.save()
    #     return instance
