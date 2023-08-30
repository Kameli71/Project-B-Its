from app import db
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime
# from sqlalchemy.dialects import mysql


class ps_configuration(db.Model):
    __tablename__ = 'ps_configuration'
    id_configuration = db.Column(
        db.Integer, primary_key=True, autoincrement=True, nullable=False)
    id_shop_group = db.Column(db.Integer)
    id_shop = db.Column(db.Integer)
    name = db.Column(db.String(254), nullable=False)
    value = db.Column(db.String())
    date_add = db.Column(DateTime(timezone=True),
                         default=func.now(), nullable=False)
    date_upd = db.Column(DateTime(timezone=True),
                         onupdate=func.now(),
                         default=func.now(),
                         nullable=False)


class ps_webservice_permission(db.Model):
    __tablename__ = 'ps_webservice_permission'
    id_webservice_permission = db.Column(
        db.Integer, primary_key=True, autoincrement=True, nullable=False)
    resource = db.Column(db.String(50), nullable=False)
    method = db.Column(db.Enum('GET', 'POST', 'PUT', 'PATCH',
                               'DELETE', 'HEAD'), nullable=False)
    id_webservice_account = db.Column(
        db.Integer, nullable=False, autoincrement=True)


class ps_webservice_account(db.Model):
    __tablename__ = 'ps_webservice_account'
    id_webservice_account = db.Column(
        db.Integer, primary_key=True, autoincrement=True, nullable=False)
    key = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String)
    class_name = db.Column(
        db.String(50), default="WebserviceRequest", nullable=False)
    is_module = db.Column(db.Integer, default=0, nullable=False)
    module_name = db.Column(db.String(50))
    active = db.Column(db.Integer, nullable=False)


class ps_webservice_account_shop(db.Model):
    __tablename__ = 'ps_webservice_account_shop'
    id_webservice_account = db.Column(
        db.Integer, primary_key=True, nullable=False, autoincrement=True)
    id_shop = db.Column(db.Integer, primary_key=True, nullable=False)
