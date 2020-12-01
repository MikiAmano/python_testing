import re


def test_contact_on_home_page(app):
    contact_on_home_page = app.contacts.get_contact_list()[0]
    contact_on_edit_page = app.contacts.get_contacts_info_from_edit_page(0)
    assert contact_on_home_page.id == contact_on_edit_page.id
    assert contact_on_home_page.firstname == contact_on_edit_page.firstname
    assert contact_on_home_page.lastname == contact_on_edit_page.lastname
    assert contact_on_home_page.all_phones_frome_home_page == merge_phones_like_on_home_page(contact_on_edit_page)
    assert contact_on_home_page.address == contact_on_edit_page.address
    assert contact_on_home_page.all_mail == merge_emails_like_on_home_page(contact_on_edit_page)

def test_contact_on_view_page(app):
    contact_on_view_page = app.contacts.get_contact_from_view_page(0)
    contact_on_edit_page = app.contacts.get_contacts_info_from_edit_page(0)
    assert contact_on_view_page.homephone == contact_on_edit_page.homephone
    assert contact_on_view_page.workphone == contact_on_edit_page.workphone
    assert contact_on_view_page.mobilephone == contact_on_edit_page.mobilephone
    assert contact_on_view_page.secondaryphone == contact_on_edit_page.secondaryphone



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



