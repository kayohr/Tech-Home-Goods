from etl import read_csv


path_file = "vendas.csv"
sale_items: list[dict]
sale_items = read_csv(path_file)
print(sale_items)
