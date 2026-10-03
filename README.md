# Task-Cloud
# Sabor do Sertão — Painel de Análise de Dados com Streamlit

## Sobre o projeto

Este projeto consiste no desenvolvimento de um painel interativo para análise de vendas da rede fictícia de lanchonetes **Sabor do Sertão**.

O painel foi desenvolvido para analisar um ano de dados de vendas das lojas localizadas em **Recife, Olinda, Caruaru, Petrolina e Garanhuns**, permitindo visualizar informações sobre faturamento, produtos, cidades, períodos de venda e formas de pagamento.

O objetivo é transformar os dados de vendas em informações visuais que possam auxiliar na análise e na tomada de decisões.

## Tecnologias utilizadas

- Python 3.10+
- Streamlit
- Pandas
- Plotly
- NumPy

## Funcionalidades

### Exploração dos dados

- Visualização das primeiras linhas do conjunto de dados;
- Resumo estatístico dos dados;
- Identificação de valores ausentes;
- Tratamento dos valores ausentes da coluna de avaliação.

### Indicadores principais

O painel apresenta quatro indicadores (KPIs):

- **Faturamento total**
- **Número de vendas**
- **Ticket médio**
- **Avaliação média**

### Filtros

Os dados podem ser filtrados por:

- Cidade;
- Categoria;
- Intervalo de datas.

Os filtros são aplicados aos indicadores e aos gráficos do painel.

### Visualizações

O projeto possui gráficos interativos para:

1. Faturamento mensal;
2. Faturamento por cidade;
3. Top 5 produtos mais vendidos em quantidade;
4. Participação das formas de pagamento.

Também pode ser utilizado um mapa de calor para analisar as vendas de acordo com o dia da semana e o horário.

### Insights

O painel apresenta conclusões obtidas a partir dos dados, permitindo identificar padrões e informações relevantes para um gestor.

Também é possível realizar o **download do conjunto de dados já filtrado** em formato CSV.

## Estrutura do projeto

sabor-do-sertao/
│
├── app.py
├── gerar_dados.py
├── requirements.txt
├── dados_vendas.csv
└── README.md

## Como executar o projeto

### 1. Clone o repositório

git clone URL_DO_SEU_REPOSITORIO

### 2. Entre na pasta do projeto

cd sabor-do-sertao

### 3. Instale as dependências

pip install -r requirements.txt

### 4. Gere os dados

Execute o arquivo responsável pela geração dos dados:

python gerar_dados.py

### 5. Execute o Streamlit

streamlit run app.py

## Objetivo da análise

O painel busca responder perguntas como:

- Em qual cidade a rede vende mais?
- Quais produtos possuem maior volume de vendas?
- Em quais períodos o faturamento é maior?
- Quais são as formas de pagamento mais utilizadas?
- Quais padrões podem ser identificados nos dados?

## Projeto acadêmico

Este projeto foi desenvolvido como atividade prática utilizando **Pair Programming**, com foco em análise e visualização de dados utilizando Python.

## Autores

**Abigail Maria Nazário e Carolline Barbosa Ferreira**

Projeto desenvolvido em dupla durante a atividade prática de análise de dados.
