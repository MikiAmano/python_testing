# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_modify_contact_firstname(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstname="test"))
    old_contacts = app.contacts.get_contact_list()
    contact = Contact(firstname="Irina", lastname="Savina")
    contact.id = old_contacts[0].id
    app.contacts.modify_first_contact(contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_contact_lastname(app):
#    if app.contacts.count() == 0:
#        app.contacts.create(Contact(firstname="test"))
#    old_contacts = app.contacts.get_contact_list()
#    app.contacts.modify_first_contact(Contact(lastname="Kuznetsova"))
#    new_contacts = app.contacts.get_contact_list()
#