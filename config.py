import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua_chave_secreta'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    MAX_CONTENT_LENGTH = 64 * 1024 * 1024  # Limite de upload de 64 MB

    # Configuração de extensões permitidas para upload
    ALLOWED_EXTENSIONS = {'csv'}

    @staticmethod
    def allowed_file(filename):
        # Função para verificar se o arquivo tem uma extensão permitida
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS
