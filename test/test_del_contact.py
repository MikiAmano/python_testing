from model.contacts import Contact


def test_delete_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstname="test"))
    app.contacts.delete_first_contact()