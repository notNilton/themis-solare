import pandas as pd

# Carregar a tabela de um arquivo CSV
file_path = './planilhas/planilha-teste.csv'  # Substitua pelo caminho do arquivo CSV
df = pd.read_csv(file_path)

# Identificar a última coluna como a coluna de e-mails
ultima_coluna = df.columns[-1]

# Remover linhas duplicadas com base na última coluna, mantendo a primeira ocorrência
df_unique = df.drop_duplicates(subset=ultima_coluna, keep="first")

# Salvar a tabela processada em um novo arquivo CSV
df_unique.to_csv('./planilhas/tabela_filtrada.csv', index=False)

print(f"Tabela processada e salva como 'tabela_filtrada.csv'. Removidas duplicatas com base na coluna '{ultima_coluna}'.")
