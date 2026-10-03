# Task-Cloud: Rede Sabor do Sertão 🌵
# Sabor do Sertão — Painel de Análise de Dados com Streamlit e Nuvem

## Sobre o projeto
Este projeto consiste no desenvolvimento e implantação em nuvem de um painel interativo para análise de vendas da rede de lanchonetes **Sabor do Sertão**.

O painel foi desenvolvido para analisar um ano de dados de vendas das lojas localizadas em **Recife, Olinda, Caruaru, Petrolina e Garanhuns**, permitindo visualizar informações sobre faturamento, produtos, cidades, períodos de venda e formas de pagamento.

O objetivo é transformar os dados de vendas em informações visuais que possam auxiliar na análise, governança e na tomada de decisões estratégicas da diretoria.


## Implantação e Infraestrutura em Nuvem (Cloud)
Para comprovar os requisitos de computação em nuvem exigidos na atividade, o painel foi implantado e está disponível publicamente:
*   **Link de Acesso Direto:** [http://20.226.59.85:8501](http://20.226.59.85:8501)
*   **Provedor de Nuvem:** Microsoft Azure (IaaS).
*   **Infraestrutura:** Instância de Máquina Virtual executando Linux Ubuntu 24.04 LTS.
*   **Segurança e Redes:** Configuração de Grupo de Segurança de Rede (NSG) com a abertura de regra de entrada para tráfego na porta **TCP 8501**.


## Tecnologias utilizadas
- Python 3.12+
- Streamlit
- Pandas
- Plotly Express
- NumPy

---

## Funcionalidades e Modificações Visuais

### Design Regional Customizado
O painel foi completamente reformulado com uma estilização CSS personalizada usando uma **paleta de cores regional em tons de terra, terracota, tangerina e areia**, trazendo a identidade visual acolhedora do Sertão Nordestino para a interface técnica.

### Geração Resiliente de Dados
O código foi modificado com um bloco de tratamento (`try/except`). Caso a planilha física `vendas.csv` não seja encontrada na pasta, o próprio algoritmo **gera de forma automatizada 5.000 registros comerciais fictícios em memória** consistentes com a realidade de operação da lanchonete, garantindo estabilidade e funcionamento ininterrupto da aplicação na nuvem.

### Indicadores principais (KPIs)
O painel apresenta três indicadores estratégicos renderizados em cartões (*cards*) estilizados com bordas em terracota:
- **Faturamento total acumulado**
- **Volume total de pedidos**
- **Ticket médio por pedido**

### Filtros
Os dados podem ser filtrados de forma dinâmica na barra lateral esquerda por:
- Unidades de Cidades da rede.

Os filtros propagam-se automaticamente, alterando de forma simultânea todos os indicadores e os gráficos do painel.

### Visualizações e Abas
O projeto foi segmentado de forma limpa em abas de navegação para melhorar a experiência do usuário (*UX*):
1.  **Desempenho de Cardápio:** Gráfico de barras horizontal mostrando as unidades vendidas por item.
2.  **Análise de Unidades:** Gráfico comparativo de faturamento por cidade.
3.  **Evolução & Pagamentos:** Linha do tempo de faturamento mensal combinada com a participação percentual das formas de pagamento em gráfico de pizza.

### Insights
O painel apresenta conclusões diretas obtidas a partir dos dados comerciais, destacando a liderança de faturamento da unidade de Recife, a alta adesão dos pratos *Tapioca Completa* e *Bolo de Rolo*, e a predominância do *Pix* como meio de pagamento.


## Estrutura do projeto na VM
```text
sabor_sertao/
│
├── app.py          # Código-fonte principal com regras visuais e dados internos
└── README.md       # Documentação técnica do projeto
```

## Como executar o projeto localmente

### 1. Clone o repositório
```bash
git clone https://github.com
```

### 2. Entre na pasta do projeto
```bash
cd Task-Cloud
```

### 3. Instale as dependências
```bash
pip install streamlit pandas plotly numpy
```

### 4. Execute o Streamlit apontando para o IP do seu servidor
```bash
python3 -m streamlit run app.py --server.address 0.0.0.0
```

## Projeto acadêmico
Este projeto foi desenvolvido como atividade prática utilizando a metodologia de **Pair Programming** (Programação em Dupla), com foco em conciliação de dados, engenharia de nuvem, governança de redes e desenvolvimento front-end com Python.

## Autores
*   **Abigail Maria Nazário**
*   **Carolline Barbosa Ferreira**
