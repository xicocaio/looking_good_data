from api.lgd.models import Order, OrderItem
import pandas as pd
import sqlalchemy as sa

# create connection to DB
con = sa.create_engine('sqlite:///db.sqlite3')

# read order data from CSV
# (na_filter=False) use NULL as blank string, avoids issues inserting on DB
df_order = pd.read_csv('orders.csv', sep=';', index_col=0, na_filter=False, skipinitialspace=True)
df_order_item = pd.read_csv('order_items.csv', sep=';', index_col=0, na_filter=False, skipinitialspace=True)

# convert date column to specific format
df_order['date'] = pd.to_datetime(df_order['date'], format="%d/%m/%Y %H:%M")
df_order['device_type'] = df_order['device_type'].str.lower()

# load data to DB
df_order.to_sql(name='lgd_order', if_exists='append', con=con)
df_order_item.to_sql(name='lgd_order_item', if_exists='append', con=con)