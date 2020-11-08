# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_add_contact(app):
    app.contacts.create(Contact(firstname="Maria", lastname="Ivanova", phone="837948273948"))

def test_add_empty_contact(app):
    app.contacts.create(Contact(firstname="", lastname="", phone=""))
