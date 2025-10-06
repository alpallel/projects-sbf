from rest_framework import serializers
from .models import User, Items

class UserSerializer(serializers.Serializer):
    user_id = serializers.UUIDField(read_only=True)
    username = serializers.CharField(max_length=100)
    user_description = serializers.CharField()
    user_password = serializers.CharField()

def create(self, validated_data):
    return User.objects.create(**validated_data)

def update(self, instance, validated_data):
    instance.username = validated_data.get("username", instance.username)
    instance.user_description = validated_data.get("user_description", instance.user_description)
    instance.save()
    return instance

class ItemsSerializer(serializers.Serializer):
    item_id = serializers.IntegerField(read_only=True)
    item_name = serializers.CharField(max_length=100)
    item_description = serializers.TextFCharField()
    price = serializers.IntegerField()
    stock = serializers.IntegerField()
    seller = UserSerializer(many=False, read_only=True)

def create(self, validated_data):
    return Items.objects.create(**validated_data)

def update(self, instance, validated_data):
    instance.item_name = validated_data.get("item_name", instance.item_name)
    instance.item_description = validated_data.get("item_description", instance.item_description)
    instance.price = validated_data.get("price", instance.price)
    instance.stock = validated_data.get("price", instance.stock)
    return instance