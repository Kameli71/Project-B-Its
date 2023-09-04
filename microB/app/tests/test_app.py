from flask import Response
import pytest
from app.app import *


def test_app():
    response = app.test_client().get("/")

    assert response.status_code == 200
    return "<h1>HELLO</h1>"


# def test_get_api_key():
#     service = "test_1"
#     response = app.test_client().get("/add_to_cart/" + service)

#     assert response.status_code == 200
#     assert isinstance(Response.get_json(response), str)