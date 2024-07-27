path_file = './data/vendas.csv'

# Cod antigo
"""
def filter_products_delivered(list_p: list[dict]) -> list[dict]:
    list_filtered_product = []
    for product in list_p:
        if product.get('entregue') == 'True':
            list_filtered_product.append(product)
    return list_filtered_product
"""

# Refatorado


def filter_products_delivered(list_p: list[dict]) -> list[dict]:
    return list(filter(lambda product: product.get('entregue') == 'True', list_p))
