# -*- coding: utf-8 -*-
import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_buy_item(app):
    app.login(username="technodeath@gmail.com", password="qwe123")
    app.find_item_on_site(item="Blouse")
    app.click_on_item(item="Blouse")
    app.click_add_to_cart()
    app.click_close_popup()
    app.logout()
