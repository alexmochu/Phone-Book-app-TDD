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

    def view_all(self):
        all_contacts = [contact for contact in self.contacts_lists]
        return all_contacts

    def delete_contact(self, contact):
        pass

    def update_contact(self, contact):
        pass
        
