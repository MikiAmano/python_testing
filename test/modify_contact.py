# -*- coding: utf-8 -*-
from model.contacts import Contact

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.modify_first_contact(Contact(firstname="Irina", lastname="Kuznetsova", phone="889857694759"))
    app.session.logout()