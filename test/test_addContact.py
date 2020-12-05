# -*- coding: utf-8 -*-
from model.contacts import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# def random_phone(maxlen):
#     symbols = string.digits + string.punctuation + " "*10
#     return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", homephone="", mobilephone="", workphone="")] + [
    Contact(firstname=random_string("firstname", 20), lastname=random_string("lastname", 20),
            homephone=random_string("homephone", 20), mobilephone=random_string("mobilephone", 20),
            workphone=random_string("workphone", 20))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.create(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


