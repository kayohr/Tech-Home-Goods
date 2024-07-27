from modules.read_csv import read_csv
from modules.filter_products_delivered import filter_products_delivered
from modules.sum_value_products import sum_value_products


def main():
    """
    Função principal para executar o processamento de vendas:
    1. Lê os dados do arquivo CSV.
    2. Filtra os produtos entregues.
    3. Calcula o valor total dos produtos entregues.
    4. Exibe o valor total.
    """
    file_path = 'data/vendas.csv'
    products = read_csv(file_path)
    delivered_products = filter_products_delivered(products)
    total_value = sum_value_products(delivered_products)
    print(f'O valor total dos produtos entregues é: {total_value}')


if __name__ == "__main__":
    main()
