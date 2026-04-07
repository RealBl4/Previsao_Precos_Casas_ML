import pandas as pd

# Carregando os dados (removi o "dados/" da frente)
treino = pd.read_csv('train.csv')

# Olhando as primeiras linhas
print(treino.head())
# Verificando informações gerais das colunas
print(treino.info())

# Verificando estatísticas básicas (média, valor mínimo, máximo)
print(treino.describe())
# Vamos escolher apenas algumas colunas numéricas para começar
# GrLivArea: Área da casa / OverallQual: Qualidade / YearBuilt: Ano de construção
colunas = ['GrLivArea', 'OverallQual', 'YearBuilt', 'SalePrice']
dados_selecionados = treino[colunas]

# Verificando se faltam dados nelas
print(dados_selecionados.isnull().sum())