# Utilisez une image Python légère comme base
FROM python:3.9-slim

# Définissez les variables d'environnement nécessaires (ajustez selon les besoins)
ENV DATABASE_URL=mysql://user123:pass123@db:3306/prestashop_db
ENV SQLALCHEMY_DATABASE_URI=mysql://user123:pass123@db:3306/prestashop_db
ENV FLASK_RUN_PORT=5000 
ENV FLASK_APP=app.py 

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY . /app
COPY ./config.py /app/config.py

COPY requirements.txt requirements.txt

# Installez les dépendances
RUN apt-get update && \
    apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    python3-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    mkdir -p /app/logs && \
    chmod 755 /app/logs

# Commande pour exécuter l'application Flask avec le port spécifié
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
