""" Import Unit Testing Library """
import unittest

from contacts import Contacts


class ContactsTestCase(unittest.TestCase):
    """ Create Contacts object test case"""
    def test_add_contacts(self):
        """ Test for adding new contacts """
        contacts = Contacts()
        response = contacts.add("alex", "0708913841")
        self.assertEqual(response, "Successfully added contacts" )