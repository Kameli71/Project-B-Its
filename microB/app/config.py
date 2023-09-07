import os, request
from flask import Flask
from decouple import config

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

PRESTASHOP_API_URL = config('API_URL')
PRESTASHOP_API_KEY = config('API_KEY')
port_gestion = "5151"
url_gestion = f"localhost:{port_gestion}/ws"

api_tmp = request.get(f'{url_gestion}/is_ws_enabled', timeout=10, verify=False)
while not bool(api_tmp.content):
    api_tmp = request.get(f'{url_gestion}is_ws_enabled', timeout=10, verify=False)
    sleep(10)
try:
    api_key_response = request.get(f"{url_gestion}/get_api_key/micro_b")
    if api_key_response.ok:
        api_key = api_key_response.text
except Exception as e:
    raise
else:
    pass
finally:
    pass