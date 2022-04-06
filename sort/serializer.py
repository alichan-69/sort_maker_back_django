from rest_framework import serializers

from .models import Sort


class SortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sort
        fields = ('id', 'name', 'description', 'image', 'user_id',
                  'delete_flg', 'create_date', 'update_date')
