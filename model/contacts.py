from sys import maxsize


class Contact:

    def __init__(self, id=None, firstname=None, lastname=None, homephone=None,
                 workphone=None, mobilephone=None, secondaryphone=None,
                 all_phones_frome_home_page=None, address=None, all_mail=None,
                 mail1=None, mail2=None, mail3=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.all_phones_frome_home_page = all_phones_frome_home_page
        self.address = address
        self.all_mail = all_mail
        self.mail1 = mail1
        self.mail2 = mail2
        self.mail3 = mail3


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize