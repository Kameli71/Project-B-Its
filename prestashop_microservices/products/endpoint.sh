#!/bin/bash

# Fonction pour redémarrer le processus principal
restart_process() {
  echo "Redémarrage du processus principal..."
  # Insérez ici la commande pour démarrer votre processus principal
}

# Gestionnaire de terminaison du conteneur
terminate() {
  echo "Arrêt du conteneur..."
  # Insérez ici des commandes pour arrêter proprement votre processus principal, si nécessaire
  exit 0
}

# Capturer le signal de terminaison
trap 'terminate' SIGTERM

# Démarrer votre processus principal
restart_process

# Boucle infinie pour garder le conteneur en vie
while true; do
  sleep 1
done