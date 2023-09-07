# from sqlalchemy import select
from app.models import ps_configuration
from app import db
from sqlalchemy.exc import NoResultFound
import uuid


RESOURCES = ['addresses', 'attachments', 'carriers', 'carts', 'cart_rules',
             'categories', 'combinations', 'configurations', 'contacts', 'countries',
             'currencies', 'customers', 'customer_threads', 'customer_messages', 'deliveries',
             'groups', 'guests', 'images', 'image_types', 'languages', 'manufacturers',
             'messages', 'order_carriers', 'order_cart_rules', 'order_details',
             'order_histories', 'order_invoices', 'orders', 'order_payments',
             'order_states', 'order_slip', 'price_ranges', 'product_features',
             'product_feature_values', 'product_options', 'product_option_values',
             'products', 'states', 'stores', 'suppliers', 'tags',
             'translated_configurations', 'weight_ranges', 'zones', 'employees',
             'search', 'content_management_system', 'shops', 'shop_groups', 'taxes',
             'stock_movements', 'stock_movement_reasons', 'warehouses', 'stocks',
             'stock_availables', 'warehouse_product_locations', 'supply_orders',
             'supply_order_details', 'supply_order_states', 'supply_order_histories',
             'supply_order_receipt_histories', 'product_suppliers', 'tax_rules',
             'tax_rule_groups', 'specific_prices', 'specific_price_rules', 'shop_urls',
             'product_customization_fields', 'customizations']

METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD']


def enable_ws():
    name = 'PS_WEBSERVICE'
    statement = db.select(ps_configuration).where(
        ps_configuration.name == name)
    ws_status = None
    try:
        ws_status = db.session.execute(statement).scalar_one()
        print(ws_status)
    except NoResultFound:
        ws_update = ps_configuration(
            name='PS_WEBSERVICE',
            value='1')
        db.session.add(ws_update)
        db.session.commit()
    finally:
        if ws_status is not None:
            return True
        return False


def random_key(str_length):
    """return a random key of length str_length"""
    random_str = str(uuid.uuid4())
    random_str = random_str.upper().replace("-", "")
    return random_str[0:str_length]
