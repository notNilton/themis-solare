import pandas as pd

def process_csv(file_path):
    """
    Processa o arquivo CSV localizado em file_path.
    Remove duplicatas na coluna 'EMAIL' e salva o arquivo processado.
    Retorna o caminho do arquivo processado ou None em caso de erro.
    """
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(file_path)
        
        # Remover duplicatas com base na coluna 'EMAIL', se a coluna existir
        if 'EMAIL' in df.columns:
            df = df.drop_duplicates(subset='EMAIL', keep='first')
        
        # Salvar o arquivo processado
        processed_file_path = file_path.replace(".csv", "_processed.csv")
        df.to_csv(processed_file_path, index=False)
        
        return processed_file_path  # Retorna o caminho do arquivo processado
    except Exception as e:
        print(f"Erro ao processar o arquivo CSV: {e}")
        return None
