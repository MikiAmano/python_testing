# -*- coding: utf-8 -*-
from model.contacts import Contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstname="test"))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Irina", lastname="Savina")
    contact.id = old_contacts[index].id
    app.contacts.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_contact_lastname(app):
#    if app.contacts.count() == 0:
#        app.contacts.create(Contact(firstname="test"))
#    old_contacts = app.contacts.get_contact_list()
#    app.contacts.modify_first_contact(Contact(lastname="Kuznetsova"))
#    new_contacts = app.contacts.get_contact_list()
#