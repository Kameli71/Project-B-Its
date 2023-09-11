# Utilisez une image Python légère comme base
FROM python:3.9-slim

# Définissez les variables d'environnement nécessaires (ajustez selon les besoins)
ENV DATABASE_URL=mysql://user123:pass123@db:3306/prestashop_db
ENV SQLALCHEMY_DATABASE_URI=sqlite:///auth.db

# Copiez les fichiers sources
COPY . /app
 
# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY requirements.txt requirements.txt

# Installez les dépendances
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/logs

RUN chmod 777 /app/logs
# Copiez le reste du code dans le conteneur
COPY . .

# Définissez la variable d'environnement pour changer le port Flask
ENV FLASK_RUN_PORT=5002

# Définir les variables d'environnement
ENV FLASK_APP=app.py 

# Commande pour exécuter l'application Flask avec le port spécifié
CMD ["flask", "run", "--host=0.0.0.0", "--port=5002"]
