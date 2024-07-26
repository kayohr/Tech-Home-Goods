import csv

path_file = 'vendas.csv'

"""]
def reader_csv(reader_file_csv: str) -> list[dict]:
    list = []
    with open(reader_file_csv, mode="r", encoding="utf-8 ") as file:
        reader = csv.DictReader(file)
        for line in reader:
            list.append(line)
    return list
"""


#Refatorando
def reader_csv(reader_file_csv: str) -> list[dict]:
    with open(reader_file_csv, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

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


def sum_value_products(list_filtered_product: list[dict]) -> int:
    total_value = 0
    for product in list_filtered_product:
        total_value += int(product.get("price"))
    return total_value

