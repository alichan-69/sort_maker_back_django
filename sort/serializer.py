from rest_framework import serializers

from .models import User, Sort, SortItem, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'delete_flg', 'access_token', 'secret', 'delete_flg',
                  'create_date', 'update_date')


class SortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sort
        fields = ('id', 'name', 'description', 'play_count', 'user',
                  'delete_flg', 'create_date', 'update_date')


class SortItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SortItem
        fields = ('id', 'name', 'sort',
                  'delete_flg', 'create_date', 'update_date')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'sort', 'user', 'delete_flg',
                  'create_date', 'update_date')
