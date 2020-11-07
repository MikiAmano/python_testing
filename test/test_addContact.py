# -*- coding: utf-8 -*-
import pytest
from model.contacts import Contact
from fixture.application_contact import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.create(Contact(firstname="Maria", lastname="Ivanova", phone="837948273948"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.create(Contact(firstname="", lastname="", phone=""))
    app.session.logout()
