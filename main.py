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

@app.route('/')
def index():
    return render_template('index.html')

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

        # Processa o CSV e obtém o caminho do arquivo processado
        processed_file_path = process_csv(file_path)
        
        # Se o processamento foi bem-sucedido, gera o link de download
        if processed_file_path:
            processed_file_url = url_for('download_file', filename=os.path.basename(processed_file_path))
            return render_template('index.html', processed_file_url=processed_file_url)
        else:
            flash('Erro ao processar o arquivo CSV')
            return redirect(url_for('index'))

    else:
        flash('Arquivo inválido. Somente arquivos CSV são permitidos.')
        return redirect(request.url)

# Rota para fazer o download do arquivo processado
@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
