from flask import Flask, render_template
import os
import json

app = Flask(__name__)

# Caminho do arquivo de recomendações
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
recommendations_file = os.path.join(base_dir, "recommender", "recommendations.json")

@app.route("/")
def home():
    try:
        # Carregar recomendações do arquivo JSON
        with open(recommendations_file, "r", encoding="utf-8") as f:
            recommendations = json.load(f)
        
        # Renderizar as recomendações na página
        return render_template("index.html", recommendations=recommendations)
    except FileNotFoundError:
        return "Arquivo de recomendações não encontrado.", 404
    except Exception as e:
        return f"Erro ao carregar as recomendações: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)