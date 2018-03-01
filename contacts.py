""" Class handles adding, updating, deleting and viewing  contacts"""
class Contacts(object):

    def __init__(self):
        """ list containing contacts """
        self.contacts_lists = []
    
    def add(self, name, phonenumber):
        """ Create contacts by holding them in an empty dictonary """
        contact_dict = {}

        contact_dict['name'] = name
        contact_dict['phonenumber'] = phonenumber
        # Add the Contacts to the contacts lists
        self.contacts_lists.append(contact_dict)
        return "Successfully added contacts"