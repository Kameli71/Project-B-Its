from flask import request, jsonify
from app import app, db
from app.models import ps_configuration, ps_webservice_account, ps_webservice_account_shop, ps_webservice_permission
from app.tools import enable_ws, random_key, RESOURCES, METHODS


@app.route("/ws/is_ws_enabled")
def is_ws_enabled():
    return enable_ws()


@app.route("/ws/get_api_key/<service_name>", methods=['GET'])
def get_api_key(service_name):
    ws_new_key = random_key(32)

    ws_new_account = ps_webservice_account(
        key=ws_new_key,
        description=service_name,
        active=1)
    db.session.add(ws_new_account)
    db.session.commit()

    statement = db.select(ps_webservice_account).where(
        ps_webservice_account.key == ws_new_key)
    ws_check_account = None
    try:
        ws_check_account = db.session.execute(statement).scalars()
        # id_webservice_account_tmp = ws_check_account.id_webservice_account
        id_webservice_account_tmp = ws_check_account.one().id_webservice_account

    finally:
        print(id_webservice_account_tmp)

    ws_new_account_shop = ps_webservice_account_shop(
        id_webservice_account=id_webservice_account_tmp,
        id_shop=1)
    db.session.add(ws_new_account_shop)
    db.session.commit()

    for resource in RESOURCES:
        for http_method in METHODS:
            permission = ps_webservice_permission(
                resource=resource,
                method=http_method,
                id_webservice_account=id_webservice_account_tmp)
            db.session.add(permission)
            db.session.commit()

    return ws_new_key
