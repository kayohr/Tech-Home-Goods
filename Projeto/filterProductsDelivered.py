from etl import read_csv, filter_products_delivered

path_file = "vendas.csv"

list_product = read_csv(path_file)
product_delivered = filter_products_delivered(list_product)
print(product_delivered)
