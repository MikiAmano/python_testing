from model.contacts import Contact


def test_delete_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstname="test"))
    old_contacts = app.contacts.get_contact_list()
    app.contacts.delete_first_contact()
    assert len(old_contacts) - 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
