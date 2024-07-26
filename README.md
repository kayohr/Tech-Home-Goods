# Tech-Home-Goods
## Descrição
Este projeto simula uma loja fictícia chamada "Tech-Home-Goods(Produtos Tecnológicos para Casa)". Ele envolve a criação de um processo ETL (Extract, Transform, Load) que lê dados de um arquivo CSV contendo uma lista de produtos, transforma esses dados conforme necessário e os carrega para serem consumidos. O objetivo é demonstrar como realizar um processo ETL usando Python.

## Estrutura do Projeto
vendas.csv: Contém a lista de produtos da loja, com o nome do produto, preço e se foi entregue ou não.
etl_process.py: Script Python que realiza o processo ETL.

## Arquivo de Dados
O arquivo vendas.csv possui o seguinte formato:
```
produto,price,entregue
cadeira,500,False
mesa,200,True
mouse,50,False
teclado,80,True
monitor,700,False
impressora,300,True
notebook,1500,False
smartphone,1000,True
tablet,600,False
caixa_de_som,150,True
pen_drive,20,False
```
## Objetivo
Realizar o processo de ETL, que inclui:

### Extração:
Leitura dos dados do arquivo CSV.
### Transformação: 
Filtragem dos produtos que não foram entregues.
### Carga: 
Disponibilização dos dados filtrados para consumo.
## Implementação
### Extração
A extração dos dados do arquivo CSV é realizada usando a biblioteca csv do Python.

### Transformação
A transformação consiste em filtrar os produtos que ainda não foram entregues.

### Carga
A carga consiste em imprimir os dados filtrados ou salvá-los em um novo arquivo CSV.