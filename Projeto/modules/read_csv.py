import csv


path_file = './data/vendas.csv'
# Cod antigo
"""]
def reader_csv(reader_file_csv: str) -> list[dict]:
    list = []
    with open(reader_file_csv, mode="r", encoding="utf-8 ") as file:
        reader = csv.DictReader(file)
        for line in reader:
            list.append(line)
    return list
"""

# Refatorado
def read_csv(read_file_csv: str) -> list[dict]:
    with open(read_file_csv, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
