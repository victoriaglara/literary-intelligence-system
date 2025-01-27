import requests
import json
import os
from dotenv import load_dotenv

# Configurar o diretório base
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

# Carregar variáveis do arquivo .env
dotenv_path = os.path.join(base_dir, ".env")
load_dotenv(dotenv_path)

# Obter a chave da API do Google Books
GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")

def fetch_reviews(book_titles, output_file):
    try:
        reviews = []
        
        # Percorrer os títulos dos livros
        for title in book_titles:
            url = f"https://www.googleapis.com/books/v1/volumes?q={title}&maxResults=3&key={GOOGLE_BOOKS_API_KEY}"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                if "items" in data:
                    for item in data["items"]:
                        volume_info = item.get("volumeInfo", {})
                        reviews.append({
                            "title": volume_info.get("title", "Título não encontrado"),
                            "authors": volume_info.get("authors", ["Autor desconhecido"]),
                            "averageRating": volume_info.get("averageRating", "Sem avaliação"),
                            "ratingsCount": volume_info.get("ratingsCount", 0),
                            "description": volume_info.get("description", "Sem descrição")
                        })
                else:
                    print(f"Sem resultados para o livro: {title}")
            else:
                print(f"Erro ao acessar a Google Books API para o livro '{title}': {response.status_code} - {response.text}")
        
        # Salvar os resultados no arquivo JSON de saída
        output_path = os.path.join(base_dir, output_file)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(reviews, f, indent=4, ensure_ascii=False)
        print(f"Dados salvos em: {output_path}")
    
    except Exception as e:
        print(f"Erro durante a busca de dados: {e}")

if __name__ == "__main__":
    # Lista de livros para buscar informações
    book_titles = [
        "The Great Gatsby",
        "1984",
        "Pride and Prejudice",
        "To Kill a Mockingbird",
        "Diary of the Fall"
    ]
    
    # Caminho para salvar o arquivo de saída
    output_file = "data/raw/raw_books.json"
    
    # Executar a função para buscar reviews
    fetch_reviews(book_titles, output_file)