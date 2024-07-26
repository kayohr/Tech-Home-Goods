import csv

path_file = 'vendas.csv'


def reader_csv(reader_file_csv: str) -> list[dict]:
    list = []
    with open(reader_file_csv, mode="r", encoding="utf-8 ") as file:
        reader = csv.DictReader(file)
        for line in reader:
            list.append(line)
    return list


"""
sale_items: list[dict]
sale_items = reader_csv(path_file)
print(sale_items)
"""

"""
def filter_products_delivered(list_p: list[dict]) -> list[dict]:
    list_filtered_product = []
    for product in list_p:
        if product.get('entregue') == 'True':
            list_filtered_product.append(product)
    return list_filtered_product
"""


#Refatorando
def filter_products_delivered(list_p: list[dict]) -> list[dict]:
    return list(filter(lambda product: product.get('entregue') == 'True', list_p))


"""
list_product = reader_csv(path_file)
product_delivered = filter_products_delivered(list_product)
print(product_delivered)
"""


"""
 lista = [2, 3, 1, 5, 1, 7, 8, 8, 9, 15, 1, 1]
 def is_not_one (value):
   return value != 1
 lista = list(filter(is_not_one, lista))
 print(lista)

lista = [2, 3, 1, 5, 1, 7, 8, 8, 9, 15, 1, 1]
lista = list(filter(lambda x: x != 1, lista))
print(lista)
"""


def sum_value_products(list_filtered_product: list[dict]) -> int:
    total_value = 0
    for product in list_filtered_product:
        total_value += int(product.get("price"))
    return total_value


"""
list_product = reader_csv(path_file)
product_delivered = filter_products_delivered(list_product)
value_products_delivered = sum_value_products(product_delivered)
print(value_products_delivered)
"""
