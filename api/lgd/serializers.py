from rest_framework import serializers
from api.lgd.models import OrderItem, Order

class CTRMetric(object):
	def __init__(self, timestamp, platform, product, ctr):
		self.timestamp = timestamp
		self.platform = platform
		self.product = product
		self.ctr = ctr

class CTRMetricSerializer(serializers.BaseSerializer):
#     def to_representation(self, obj):
#     return {
#         'timestamp': obj.timestamp,
#         'platform': obj.device_type,
#         'product': obj.code_color,
#         'ctr': obj.ctr
#     }
	# order =  OrderSerializer()
	# timestamp = serializers.TimeField()
	# platform = 

	class Meta:
		model = CTRMetric

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ('__all__')

class OrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		fields = ('code_color')
