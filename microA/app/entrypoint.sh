#!/bin/bash

# restart_process() {
#     echo "Redémarrage du processus principal..."
# }

# terminate() {
#     echo "Arrêt du conteneur..."
#     exit 0
# }

# trap 'terminate' SIGTERM
# restart_process

# while true; do
#     sleep 1
# done
gunicorn -b 0.0.0.0:5000 app:app