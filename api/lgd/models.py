from django.db import models
from django.db import connection
from collections import namedtuple


def order_qty_sql(start_date, end_date, interval, product, platform):
	# aggregates product sales in date range with defined intervals
    with connection.cursor() as cursor:
        sql_initial = """
			SELECT datetime(CAST((strftime('%%s', lgd_order.date) - strftime('%%s', %s)) / %s AS integer) * %s + strftime('%%s', %s), 'unixepoch') AS agg_date,
       				sum(lgd_order_item.quantity) AS qty,
       				lgd_order_item.code_color,
       				lgd_order.device_type
			FROM lgd_order
			LEFT JOIN lgd_order_item ON lgd_order.id = lgd_order_item.order_id
			WHERE lgd_order.date >= %s
  				AND lgd_order.date < %s
			"""

        sql_extra_conditions = ""

        sql_final = """
			GROUP BY agg_date,
         			lgd_order_item.code_color,
         			lgd_order.device_type
			"""

        params = [start_date, interval, interval,
                  start_date, start_date, end_date]

        # appending optional parameters to query
        if product:
            sql_extra_conditions += """ AND lgd_order_item.code_color = %s """
            params.append(product)

        if platform:
            sql_extra_conditions += """ AND lower(lgd_order.device_type) = lower(%s) """
            params.append(platform)

        cursor.execute(sql_initial + sql_extra_conditions + sql_final,
                       params)

        return namedtuplefetchall(cursor)


def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


class Order(models.Model):
    user_id = models.IntegerField()
    date = models.DateTimeField(db_index=True)
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
    device_type = models.CharField(db_index=True, max_length=200)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    sku = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    code_color = models.CharField(db_index=True, max_length=200)

    def __str__(self):
        return self.sku

    class Meta:
        db_table = 'lgd_order_item'
