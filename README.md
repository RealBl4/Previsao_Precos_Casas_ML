
# 🏠 Previsão de Preços de Casas - Machine Learning

> 🚀 **[CLIQUE AQUI PARA VER O PROJETO COMPLETO COM GRÁFICOS INTERATIVOS](https://nbviewer.org/github/RealBl4/Previsao_Precos_Casas_ML/blob/main/projeto_previsao.ipynb)**

Este projeto utiliza **Regressão Linear** para prever o preço de venda de imóveis...

Este projeto utiliza **Regressão Linear** para prever o preço de venda de imóveis com base em características estruturais e localização. O dataset utilizado é o famoso *Ames Housing Dataset* (Kaggle).

## 🚀 Resultados
O modelo final atingiu um **R² Score de 0.8213**, demonstrando que as variáveis selecionadas explicam mais de 82% da variação dos preços.

## 🛠️ Tecnologias Utilizadas
* **Python 3**
* **Pandas**: Manipulação de dados.
* **Scikit-Learn**: Criação do modelo de Machine Learning e métricas.
* **Seaborn/Matplotlib**: Visualização de dados e correlações.

## 📊 Visualização do Modelo
Abaixo, a relação entre os preços reais e as previsões feitas pelo modelo:

![Gráfico de Previsão](resultado_previsao.png)

## 🧠 Insights de Engenharia de Dados
* A inclusão da variável de **Bairro (Neighborhood)** foi crucial para aumentar a precisão do modelo.
* Variáveis como **Qualidade Geral (OverallQual)** e **Área Construída (GrLivArea)** possuem a maior correlação com o preço final.