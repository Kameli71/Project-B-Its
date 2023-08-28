import requests
from config import PRESTASHOP_API_URL, PRESTASHOP_API_KEY
# from views import cache

headers = {
'Authorization': f'Basic {PRESTASHOP_API_KEY}'
}

# @cache.memoize(timeout=300)
def fetch_product(product_id):
    response = requests.get(f'{PRESTASHOP_API_URL}/products/{product_id}', headers=headers)
    if response.status_code == 200:
        return response.json()
    return "allo"
