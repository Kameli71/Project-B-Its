from flask import Response
from app import app
import pytest
from app.views import *


def test_is_ws_enabled():
    response = app.test_client().get("/ws/is_ws_enabled")

    assert response.status_code == 200
    # assert Response.get_json(response)


def test_get_api_key():
    service = "test_1"
    response = app.test_client().get("/ws/get_api_key/" + service)

    assert response.status_code == 200
    assert isinstance(Response.get_json(response), str)
