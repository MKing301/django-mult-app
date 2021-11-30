from django.test import TestCase
from .models import Contact


class ContactTestCase(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@gmail.com",
            user_request="This is a test"
        )

    def test_contact_str(self):
        user = self.contact
        self.assertTrue(isinstance(user, Contact))
        self.assertEqual(str(user), "Jane Doe")
