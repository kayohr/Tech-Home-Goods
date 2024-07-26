from etl import reader_csv, filter_products_delivered

path_file = "vendas.csv"

list_product = reader_csv(path_file)
product_delivered = filter_products_delivered(list_product)
print(product_delivered)
