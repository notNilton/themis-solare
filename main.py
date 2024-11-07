from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename
import os
from app.routes import routes
from config import Config
from app.utils import process_csv  # Importa a função process_csv

# Inicializa a aplicação Flask
app = Flask(__name__)
app.config.from_object(Config)

# Certifique-se de que a pasta de uploads existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Registre o blueprint (se estiver usando)
app.register_blueprint(routes)

# Rota principal que serve o index.html
@app.route('/')
def index():
    # Renderiza o arquivo index.html da pasta 'templates'
    return render_template('index.html')

# Rota para receber e processar o arquivo CSV
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('Nenhum arquivo selecionado')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('Nenhum arquivo selecionado')
        return redirect(request.url)

    if file and Config.allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        flash('Arquivo enviado com sucesso')

        # Processar o CSV
        processed_file_path = process_csv(file_path)
        if processed_file_path:
            flash('Arquivo CSV processado com sucesso')
        else:
            flash('Erro ao processar o arquivo CSV')

        return redirect(url_for('index'))

    else:
        flash('Arquivo inválido. Somente arquivos CSV são permitidos.')
        return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
