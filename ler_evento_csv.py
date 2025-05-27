import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo 'Erro Aplicativo.csv' e 'Erro Sistema.csv' pela leitura de arquivos .csv no pacote pandas
dfEA = pd.read_csv('Erro Aplicativo.csv', sep=',', encoding='utf-8', index_col=False)
dfES = pd.read_csv('Erro Sistema.csv', sep=',', encoding='utf-8', index_col=False)

# Verifica as colunas
print("Colunas Aplicativo:", dfEA.columns)
print("Colunas Sistema:", dfES.columns)

# Reseta o index
dfEA = dfEA.reset_index(drop=True)
dfES = dfES.reset_index(drop=True)

# Trata a coluna de Identificação do Evento para numero ou string
dfEA['Identificação do Evento'] = dfEA['Identificação do Evento'].astype(str).str.strip()
dfES['Identificação do Evento'] = dfES['Identificação do Evento'].astype(str).str.strip()

# Conta e retorna os top 10 da coluna Identificação do Evento
event_counts_aplicativo = dfEA['Identificação do Evento'].value_counts().head(10)
event_counts_sistema = dfES['Identificação do Evento'].value_counts().head(10)

# Renderiza 'Erro Aplicativo.csv'
plt.figure(figsize=(10, 6))
event_counts_aplicativo.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 10 - Contagem por Identificação do Evento em Aplicativo')
plt.xlabel('Identificação do Evento')
plt.ylabel('Número de Ocorrências')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Renderiza 'Erro Aplicativo.csv'
plt.figure(figsize=(10, 6))
event_counts_sistema.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 10 - Contagem por Identificação do Evento em Sistema')
plt.xlabel('Identificação do Evento')
plt.ylabel('Número de Ocorrências')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()