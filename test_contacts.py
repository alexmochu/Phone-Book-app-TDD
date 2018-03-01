""" Import Unit Testing Library """
import unittest

from contacts import Contacts


class ContactsTestCase(unittest.TestCase):

    def setUp(self):
        """ Setting up Contacts class """
        self.contacts = Contacts()

    def tearDown(self):
        """ Removing Contacts class """
        del self.contacts

    """ Create Contacts object test case"""
    def test_add_contacts(self):
        """ Test for adding new contacts """
        response = self.contacts.add("alex", "0708913841")
        self.assertEqual(response, "Successfully added contacts" )

    """ Create Contacts object test case"""
    def test_view_all_contacts(self):
        # Create contact list
        self.contacts.contacts_lists = [{"name": "Tecky", "phonenumber": "123456789"},{"name": "Mazo", "phonenumber": "987654321"}]
        response = self.contacts.contacts_lists
        value = self.contacts.view_all()
        self.assertEqual(response, value )

    """ Delete Contacts object test case"""
    def test_delete_contact(self):
        # Create contact list
        self.contacts.contacts_lists = [{"name": "Tecky", "phonenumber": "123456789"}]
        self.assertEqual(1, len(self.contacts.contacts_lists))
        self.contacts.delete_contact("Tecky")
        self.assertEqual(0, len(self.contacts.contacts_lists))

    """ Update Contacts name object test case"""
    def test_update_name_of_contact(self):
        # Create contact list
        self.contacts.contacts_lists = [{"name": "Tecky", "phonenumber": "123456789"}]
        contact_in_list = self.contacts.contacts_lists[0]
        contact_in_list["name"] = "Mario"
        self.contacts.update_contact(contact_in_list["name"])
        self.assertEqual(contact_in_list["name"], self.contacts.contacts_lists["name"])
        
    """ Update Contacts phonenumber object test case"""
    def test_update_phonenumber_of_contact(self):
        # Create contact list
        self.contacts.contacts_lists = [{"name": "Tecky", "phonenumber": "123456789"}]
        contact_in_list = self.contacts.contacts_lists[0]
        contact_in_list["phonenumber"] = "Mario"
        self.contacts.update_contact(contact_in_list["phonenumber"])
        self.assertEqual(contact_in_list["phonenumber"], self.contacts.contacts_lists["name"])
        