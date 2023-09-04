import requests
import base64
import xmltodict
from config import PRESTASHOP_API_URL, PRESTASHOP_API_KEY

presta_key = base64.b64encode(
    PRESTASHOP_API_KEY.encode("utf-8")).decode("utf-8")
headers = {
    'Authorization': f'Basic {presta_key}'
}

def fetch_product(product_id):
    response = requests.get(f'http://{PRESTASHOP_API_URL}/api/products/{product_id}', headers=headers)
    if response.status_code == 200:
        try:
            product_data_xml = response.content.decode("utf-8")
            product_data_dict = xmltodict.parse(product_data_xml)
            return product_data_dict
        except Exception as e:
            return {"error": f"Failed to parse XML: {e}"}
    return {"error": "Failed to fetch product data from PrestaShop"}