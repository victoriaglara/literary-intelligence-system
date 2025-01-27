## Alteração para Google Books API

Com a descontinuação da API do Goodreads, o projeto agora utiliza a Google Books API para buscar informações sobre livros. O script `fetch_goodreads_review.py` foi renomeado para `fetch_google_books_reviews.py`.

### Configuração
1. Crie um projeto no Google Cloud Console.
2. Ative a Google Books API e gere uma chave de API.
3. Configure a chave de API no arquivo `.env` ou no script diretamente.

### Como Rodar
1. Ative o ambiente virtual:
