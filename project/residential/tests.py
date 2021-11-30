from django.test import TestCase
from .models import Vendor


class VendorTestCase(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="BioTurf",
            address="1234 Main St",
            city="Raleigh",
            vendor_state="NC",
            postal_code="27601",
            office_number="9197779311",
            email="bioturf@company.com",
            website="bioturf.com"
        )

    def test_vendor_str(self):
        company = self.vendor
        self.assertTrue(isinstance(company, Vendor))
        self.assertEqual(str(company), "BioTurf")
