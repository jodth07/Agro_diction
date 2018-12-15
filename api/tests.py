from django.test import TestCase
from .models import Contact


class ContactTestCase(TestCase:
    def setUp(self):
        Contact.objects.create(first_name="Jake", last_name="Peralta")
        Contact.objects.create(first_name="Amie", last_name="Santiago")
        Contact.objects.create(first_name="Rosa", last_name="Diaz")
        
    def test_contact_last_name(self):
        jake = Contact.objects.get(first_name="Jake")
        amie = Contact.objects.get(first_name="Amie")
        self.assertEqual(jake.last_name, "Peralta")
        self.assertEqual(amie.last_name, "Santiago")