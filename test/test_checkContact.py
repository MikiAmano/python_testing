import re
from random import randrange


def test_contact_on_home_page(app):
    all_contacts = app.contacts.get_contact_list()
    index = randrange(len(all_contacts))
    app.contacts.open_contact_to_edit_by_index(index)
    contact_on_home_page = app.contacts.get_contact_list()[0]
    contact_on_edit_page = app.contacts.get_contacts_info_from_edit_page(0)
    assert contact_on_home_page.id == contact_on_edit_page.id
    assert contact_on_home_page.firstname == contact_on_edit_page.firstname
    assert contact_on_home_page.lastname == contact_on_edit_page.lastname
    assert contact_on_home_page.all_phones_frome_home_page == merge_phones_like_on_home_page(contact_on_edit_page)
    assert contact_on_home_page.address == contact_on_edit_page.address
    assert contact_on_home_page.all_mail == merge_emails_like_on_home_page(contact_on_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone,
                                        contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.mail1, contact.mail2, contact.mail3]))))



