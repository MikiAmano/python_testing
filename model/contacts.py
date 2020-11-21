from sys import maxsize


class Contact:

    def __init__(self, id=None, firstname=None, lastname=None, homephone=None,
                 workphone=None, mobilephone=None, all_phones_frome_home_page=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.all_phones_frome_home_page = all_phones_frome_home_page


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize