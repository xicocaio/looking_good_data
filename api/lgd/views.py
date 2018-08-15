from api.lgd.models import Order, OrderItem
from api.lgd.serializers import CTRMetricSerializer, OrderSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import pytz

class CTR(APIView):
    def get(self, request, format=None):
    	# getting query_params
        start_timestamp = pytz.utc.localize(datetime.strptime(request.GET.get('startTimestamp'), '%Y-%m-%d %H:%M:%S'))
        end_timestamp = pytz.utc.localize(datetime.strptime(request.GET.get('endTimestamp'), '%Y-%m-%d %H:%M:%S'))
        aggregation = request.GET.get('aggregation')
        product = request.GET.get('product')
        platform = request.GET.get('platform')

        # select only PDVs that cover the location provided
        # and order them by distance, selecting only the nearest
        orders = Order.objects.filter(date__range=[start_timestamp, end_timestamp])
                   # .annotate(distance=Distance('address', point)) \
                   # .order_by('distance', 'id')[:1]


        # orders = Order.objects.all()

        # could return only a object but, to guarantee scalability
        # preferred to always use list
        serializer = OrderSerializer(orders, many=True)
        custom_data = {'orders': serializer.data}
        return Response(custom_data)
