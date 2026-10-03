import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta

# Configuração da página e identidade visual
st.set_page_config(
    page_title="Sabor do Sertão — Painel Comercial",
    page_icon="🌵",
    layout="wide"
)


st.markdown("""
    <style>
    /* Estilização dos blocos de métricas e cartões */
    .card-sertao {
        background-color: #fdfaf4;
        border-left: 5px solid #d45d34;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .card-titulo {
        color: #5c3a21;
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 5px;
    }
    .card-valor {
        color: #d45d34;
        font-size: 2.2rem;
        font-weight: 800;
    }
    /* Estilo geral dos títulos */
    h1, h2, h3 {
        color: #4a2c11 !important;
        font-family: 'Georgia', serif;
    }
    </style>
""", unsafe_allow_html=True)

# Define a paleta de cores Nordestina para os gráficos do Plotly
PALETA_SERTAO = ["#d45d34", "#e99a4c", "#6c844c", "#a25934", "#edd09e", "#8c6c4c"]

@st.cache_data
def carregar_dados():
    try:
        df = pd.read_csv("vendas.csv", parse_dates=["data"])
    except FileNotFoundError:
        np.random.seed(42)
        n_vendas = 5000

        cidades = ["Recife", "Olinda", "Caruaru", "Petrolina", "Garanhuns"]
        produtos = ["Bolo de Rolo", "Cartola", "Tapioca Completa", "Cuscuz Recheado", "Suco de Umbu"]
        precos = [25.00, 18.00, 12.00, 15.00, 7.00]
        pagamentos = ["Pix", "Cartão de Crédito", "Cartão de Débito", "Dinheiro"]

        data_inicial = datetime(2026, 1, 1)
        datas = [data_inicial + timedelta(days=int(np.random.randint(0, 270))) for _ in range(n_vendas)]

        lista_cidades = np.random.choice(cidades, n_vendas, p=[0.35, 0.20, 0.15, 0.18, 0.12])
        lista_produtos = np.random.choice(produtos, n_vendas, p=[0.25, 0.20, 0.30, 0.15, 0.10])
        lista_pagamentos = np.random.choice(pagamentos, n_vendas, p=[0.45, 0.30, 0.15, 0.10])

        df = pd.DataFrame({
            "data": datas,
            "cidade": lista_cidades,
            "produto": lista_produtos,
            "forma_pagamento": lista_pagamentos
        })

        mapa_precos = dict(zip(produtos, precos))
        df["preco_unitario"] = df["produto"].map(mapa_precos)
        df["quantidade"] = np.random.randint(1, 4, n_vendas)
        df["valor_total"] = df["preco_unitario"] * df["quantidade"]
    return df

df = carregar_dados()


st.image("https://unsplash.com", width='stretch')

st.title("🌵 Rede Sabor do Sertão")
st.markdown("### *Painel Estratégico de Desempenho Comercial*")
st.markdown("Bem-vindo ao centro de inteligência analítica. Use os filtros laterais para navegar pelos indicadores.")

st.sidebar.markdown("## 🏜️ Filtros do Sertão")
cidades_selecionadas = st.sidebar.multiselect(
    "Selecione as Unidades:",
    options=df["cidade"].unique(),
    default=df["cidade"].unique()
)

# Filtro dinâmico do DataFrame
df_filtrado = df[df["cidade"].isin(cidades_selecionadas)]


faturamento_total = df_filtrado["valor_total"].sum()
total_pedidos = df_filtrado.shape[0]
ticket_medio = faturamento_total / total_pedidos if total_pedidos > 0 else 0

col_m1, col_m2, col_m3 = st.columns(3)

with col_m1:
    st.markdown(f"""
        <div class="card-sertao">
            <div class="card-titulo">Faturamento Acumulado</div>
            <div class="card-valor">R$ {faturamento_total:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with col_m2:
    st.markdown(f"""
        <div class="card-sertao">
            <div class="card-titulo">Volume de Pedidos</div>
            <div class="card-valor">{total_pedidos:,}</div>
        </div>
    """, unsafe_allow_html=True)

with col_m3:
    st.markdown(f"""
        <div class="card-sertao">
            <div class="card-titulo">🍽️Ticket Médio por Pedido</div>
            <div class="card-valor">R$ {ticket_medio:.2f}</div>
        </div>
    """, unsafe_allow_html=True)

aba_produtos, aba_regioes, aba_tempo = st.tabs([
    "Desempenho de Cardápio",
    "Análise de Unidades",
    "Evolução & Pagamentos"
])


with aba_produtos:
    st.markdown("### Quais são os produtos mais desejados?")
    col_p1, col_p2 = st.columns([2, 1])

    with col_p1:
        volume_produto = df_filtrado.groupby("produto")["quantidade"].sum().reset_index().sort_values(by="quantidade", ascending=True)
        fig_o_que = px.bar(
            volume_produto, x="quantidade", y="produto", orientation="h",
            labels={"quantidade": "Unidades Vendidas", "produto": "Item do Cardápio"},
            color="produto", color_discrete_sequence=PALETA_SERTAO
        )
        fig_o_que.update_layout(showlegend=False, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_o_que, use_container_width=True)

    with col_p2:
        st.markdown("#### Insights do Cardápio")
        st.info("""
            * **Líder de Vendas:** A **Tapioca Completa** e o **Bolo de Rolo** lideram a preferência do público nas capitais.
            * **Oportunidade:** O *Suco de Umbu*, embora possua menor faturamento individual, apresenta excelente volume de saída casado com pratos salgados.
        """)


with aba_regioes:
    st.markdown("### Onde estão nossos maiores mercados?")
    faturamento_cidade = df_filtrado.groupby("cidade")["valor_total"].sum().reset_index().sort_values(by="valor_total", ascending=False)

    fig_onde = px.bar(
        faturamento_cidade, x="cidade", y="valor_total",
        labels={"cidade": "Unidade Regional", "valor_total": "Faturamento Líquido (R$)"},
        color="cidade", color_discrete_sequence=PALETA_SERTAO
    )
    fig_onde.update_layout(showlegend=False, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_onde, use_container_width=True)


with aba_tempo:
    col_t1, col_t2 = st.columns(2)

    with col_t1:
        st.markdown("### Linha do Tempo (Faturamento Mensal)")
        df_filtrado["mes"] = df_filtrado["data"].dt.to_period("M").astype(str)
        faturamento_mensal = df_filtrado.groupby("mes")["valor_total"].sum().reset_index()

        # Correção definitiva do Plotly px.line removendo o argumento conflitante
        fig_quando = px.line(
            faturamento_mensal, x="mes", y="valor_total",
            labels={"mes": "Período Operacional", "valor_total": "Faturamento (R$)"},
            color_discrete_sequence=[PALETA_SERTAO[0]]
        )
        fig_quando.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_quando, use_container_width=True)

    with col_t2:
        st.markdown("### Preferência de Meios de Pagamento")
        pagamento_resumo = df_filtrado.groupby("forma_pagamento")["valor_total"].sum().reset_index()

        fig_como = px.pie(
            pagamento_resumo, values="valor_total", names="forma_pagamento",
            color_discrete_sequence=PALETA_SERTAO
        )
        fig_como.update_layout(paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_como, use_container_width=True)
