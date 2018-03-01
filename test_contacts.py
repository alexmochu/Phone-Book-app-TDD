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

    def test_view_all_contacts(self):
        self.contacts.contacts_lists = [{"name": "Tecky", "phonenumber": "123456789"},{"name": "Mazo", "phonenumber": "987654321"}]
        response = self.contacts.contacts_lists
        value = self.contacts.view_all()
        self.assertEqual(response, value )

    def test_delete_contact(self):
        self.contacts.contacts_lists = [{"name": "Tecky", "phonenumber": "123456789"}]
        self.assertEqual(1, len(self.contacts.contacts_lists))
        self.contacts.delete_contact("Tecky")
        self.assertEqual(0, len(self.contacts.contacts_lists))

    def test_update_name_of_contact(self):
        pass

    def test_update_phonenumber_of_contact(self):
        pass