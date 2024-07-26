from etl import reader_csv


path_file = "vendas.csv"
sale_items: list[dict]
sale_items = reader_csv(path_file)
print(sale_items)
