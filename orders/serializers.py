from rest_framework import serializers

from .models import Order, OrderItem, Table
from menu.models import MenuItem


class OrderItemCreateSerializer(serializers.Serializer):

    menu_item = serializers.IntegerField()

    quantity = serializers.IntegerField()


class OrderCreateSerializer(serializers.Serializer):

    table_id = serializers.IntegerField()

    items = OrderItemCreateSerializer(many=True)