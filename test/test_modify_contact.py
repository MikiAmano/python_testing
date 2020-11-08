# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_modify_contact_firstname(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstname="test"))
    app.contacts.modify_first_contact(Contact(firstname="Irina"))

def test_modify_contact_lastname(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstname="test"))
    app.contacts.modify_first_contact(Contact(lastname="Kuznetsova"))