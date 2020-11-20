from model.contacts import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def change_fill_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contacts):
        wd = self.app.wd
        self.change_fill_value("firstname", contacts.firstname)
        self.change_fill_value("lastname", contacts.lastname)
        self.change_fill_value("home", contacts.phone)

    def create(self, contacts):
        wd = self.app.wd
        self.open_new_contact_page()
        self.fill_contact_form(contacts)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        wd.implicitly_wait(5)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_css_selector("[value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.implicitly_wait(5)
        wd.find_element_by_css_selector("div.msgbox")
        wd.implicitly_wait(5)

    def modify_first_contact(self, new_contact_date):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_css_selector("[title='Edit']").click()
        self.fill_contact_form(new_contact_date)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contacts_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("[name='entry']"):
            family_name = element.find_element_by_css_selector("td:nth-child(2)").text
            name = element.find_element_by_css_selector("td:nth-child(3)").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(id=id, firstname=name, lastname=family_name))
        return contacts
