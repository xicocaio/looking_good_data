from django.db import models

from django.db import models

class Order(models.Model):
	user_id = models.IntegerField()
	date = models.DateTimeField()
	subtotal = models.FloatField()
	discount = models.FloatField(default=0)
	total = models.FloatField()
	status = models.CharField(max_length=200)
	payment_type = models.CharField(max_length=200)
	shipping_cost = models.FloatField()
	shipping_service = models.CharField(max_length=200)
	address_city = models.CharField(max_length=100)
	address_state = models.CharField(max_length=10)
	utm_source_medium = models.CharField(max_length=200)
	device_type = models.CharField(max_length=200)

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	sku = models.CharField(max_length=200)
	quantity = models.IntegerField(default=1)
	code_color = models.CharField(max_length=200)

	def __str__(self):
		return self.sku

	class Meta:
		db_table = 'lgd_order_item'

