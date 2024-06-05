import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')

 # Adicionar um cabeçalho ao aplicativo
st.header('Análise de Veículos a Venda')


# Função para extrair a marca do modelo
def extrair_marca(modelo):
    # Divida o modelo em palavras usando um separador (ex.: espaço)
    palavras = modelo.split(' ')
    # A marca geralmente é a primeira palavra
    marca = palavras[0]
    return marca

# Exibir os dados carregados
st.write(car_data)

# Botão para criar um histograma
hist_button = st.button('Criar histograma')

if hist_button:
# Mensagem ao clicar no botão
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

 # Criar um histograma
    fig = px.histogram(car_data, x="odometer", title='Distribuição da Quilometragem dos Veículos à Venda')

 # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)




# Distribuição do ano do modelo por condição
st.subheader('Distribuição do Ano do Modelo por Condição')
# Criar o histograma com a coluna 'model_year' e agrupar por 'condition'
fig_hist_year = px.histogram(car_data, x='model_year', color='condition', title='Distribuição de Anos de Modelo por Condição')
# Personalizar o layout do gráfico
fig_hist_year.update_layout(
    xaxis_title='Ano de Modelo',
    yaxis_title='Frequência',
)
# Exibir o gráfico
st.plotly_chart(fig_hist_year, use_container_width=True)


# Botão para criar um gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
 # Mensagem ao clicar no botão
   st.write('Criando um gráfico de dispersão para Quilometragem vs Preço')

 # Criar um gráfico de dispersão
   fig = px.scatter(car_data, x='odometer', y='price', title='Quilometragem vs Preço dos Veículos',
labels={'odometer': 'Quilometragem (milhas)', 'price': 'Preço (USD)'})

# Exibir um gráfico Plotly interativo
   st.plotly_chart(fig, use_container_width=True)