from sqlalchemy import select
from app.models import ps_configuration
from app import db
from sqlalchemy.exc import NoResultFound


def enable_ws():
    name = 'PS_WEBSERVICE'
    statement = db.select(ps_configuration).where(
        ps_configuration.name == name)
    ws_status = None
    try:
        ws_status = db.session.execute(statement).scalar_one()
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
