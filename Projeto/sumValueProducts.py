from etl import reader_csv, filter_products_delivered, sum_value_products

path_file = "vendas.csv"

list_product = reader_csv(path_file)
product_delivered = filter_products_delivered(list_product)
value_products_delivered = sum_value_products(product_delivered)
print(value_products_delivered)
