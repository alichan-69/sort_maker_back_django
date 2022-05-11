from rest_framework import serializers

from .models import Sort, SortItem


class SortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sort
        fields = ('id', 'name', 'description', 'image', 'user_id',
                  'delete_flg', 'create_date', 'update_date')


class SortItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SortItem
        fields = ('id', 'name', 'image', 'sort',
                  'delete_flg', 'create_date', 'update_date')
