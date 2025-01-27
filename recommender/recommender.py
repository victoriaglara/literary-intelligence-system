from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Caminho para o arquivo de recomendações
base_dir = os.path.dirname(os.path.abspath(__file__))
recommendations_file = os.path.join(base_dir, "recommendations.json")

@app.route("/")
def home():
    try:
        # Carrega as recomendações do arquivo JSON
        with open(recommendations_file, "r", encoding="utf-8") as f:
            recommendations = json.load(f)
        
        # Corrige a exibição dos autores (garante que nomes estejam como strings)
        for book in recommendations:
            if isinstance(book["authors"], list):  # Se for lista
                book["authors"] = ", ".join(book["authors"])  # Junta como string
            elif isinstance(book["authors"], str):  # Se já for string
                book["authors"] = book["authors"].strip()  # Garante que está limpa
            else:  # Caso contrário (erro inesperado)
                book["authors"] = "Autor desconhecido"

        return render_template("index.html", recommendations=recommendations)

    except FileNotFoundError:
        return "Arquivo de recomendações não encontrado."
    except Exception as e:
        return f"Erro ao carregar recomendações: {str(e)}"

@app.route("/api/recommendations", methods=["GET"])
def api_recommendations():
    try:
        # Retorna o conteúdo do arquivo JSON como API
        with open(recommendations_file, "r", encoding="utf-8") as f:
            recommendations = json.load(f)
        return jsonify(recommendations)
    except FileNotFoundError:
        return jsonify({"error": "Arquivo de recomendações não encontrado."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)