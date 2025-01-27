import os
import pandas as pd
from dotenv import load_dotenv

# Carregar variáveis do .env na raiz
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Diretório raiz
dotenv_path = os.path.join(base_dir, '.env')
load_dotenv(dotenv_path)

#Descobrir de onde está vindo o erro de diretório

print(f"Base Directory Calculado: {os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))}")
print(f"Arquivos no Diretório Atual: {os.listdir(os.getcwd())}")
print(f"Arquivos no Base Dir: {os.listdir(base_dir)}")

# Caminho do arquivo de entrada e saída
input_file = os.path.join(base_dir, "data", "raw", "raw_books.json")
output_file = os.path.join(base_dir, "data", "processed", "books.csv")

def preprocess_data():
    try:
        # Verificar se o arquivo de entrada existe
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Arquivo de entrada não encontrado: {input_file}")

        # Carregar dados brutos do JSON
        print(f"Lendo dados de: {input_file}")
        raw_data = pd.read_json(input_file)

        # Exibir algumas linhas dos dados brutos
        print("Pré-visualização dos dados brutos:")
        print(raw_data.head())

        # Processar dados relevantes (ajuste conforme necessário)
        processed_data = raw_data[[
            "title",
            "authors",
            "averageRating",
            "ratingsCount",
            "description"
        ]].dropna()

        # Exibir algumas linhas dos dados processados
        print("Pré-visualização dos dados processados:")
        print(processed_data.head())

        # Salvar os dados processados no CSV
        processed_data.to_csv(output_file, index=False)
        print(f"Dados processados salvos em: {output_file}")

    except Exception as e:
        print(f"Erro durante o processamento dos dados: {e}")

if __name__ == "__main__":
    preprocess_data()