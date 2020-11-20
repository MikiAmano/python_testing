# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_add_contact(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contact(firstname="Maria", lastname="Ivanova", phone="837948273948")
    app.contacts.create(contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_add_empty_contact(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contact(firstname="", lastname="", phone="")
    app.contacts.create(contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
