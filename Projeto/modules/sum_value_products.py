path_file = './data/vendas.csv'


def sum_value_products(list_filtered_product: list[dict]) -> int:
    total_value = 0
    for product in list_filtered_product:
        total_value += int(product.get("price"))
    return total_value
