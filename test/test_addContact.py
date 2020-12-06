# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contacts.get_contact_list()
    app.contacts.create(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


