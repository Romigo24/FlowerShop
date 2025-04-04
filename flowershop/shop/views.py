from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from django.http import HttpResponse


@api_view(['GET'])
def sales_statistics(request):
    orders = Order.objects.all().select_related('customer', 'bouquet')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)



def index(request):
    return HttpResponse("Hello, World!")