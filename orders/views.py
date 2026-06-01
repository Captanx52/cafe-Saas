from decimal import Decimal

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Order, OrderItem, Table
from .serializers import OrderCreateSerializer

from menu.models import MenuItem


class CreateOrderAPIView(APIView):

    def post(self, request):

        serializer = OrderCreateSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        table_id = serializer.validated_data['table_id']

        items_data = serializer.validated_data['items']

        table = Table.objects.get(id=table_id)

        order = Order.objects.create(
            cafe=table.cafe,
            table=table,
        )

        total_price = Decimal('0.00')

        for item_data in items_data:

            menu_item = MenuItem.objects.get(
                id=item_data['menu_item']
            )

            quantity = item_data['quantity']

            item_total = menu_item.price * quantity

            total_price += item_total

            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=quantity,
                price=menu_item.price
            )

        order.total_price = total_price

        order.save()

        return Response(
            {
                'message': 'Order created successfully',
                'order_id': order.id,
                'total_price': total_price
            },
            status=status.HTTP_201_CREATED
        )