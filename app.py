import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('C:/Users/PC/Documents/projetos/projeto-1/vehicles.csv')

 # Adicionar um cabeçalho ao aplicativo
st.header('Análise de Veículos à Venda')

# Botão para criar um histograma
hist_button = st.button('Criar histograma')

if hist_button:
    # Mensagem ao clicar no botão
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # Criar um histograma
    fig = px.histogram(car_data, x="odometer", title='Distribuição da Quilometragem dos Veículos à Venda')
    
    # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

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
            