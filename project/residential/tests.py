import datetime

from django.test import TestCase
from .models import Vendor, Task


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


class TaskTestCase(TestCase):
    def test_task_str(self):
        _vendor = Vendor.objects.create(
            name="SpringGreen",
            address="1234 Main St",
            city="Raleigh",
            vendor_state="NC",
            postal_code="27601",
            office_number="9197779311",
            email="sp@company.com",
            website="sp.com"
        )

        _task = Task.objects.create(
            task_date=datetime.date(1997, 10, 19),
            name="Test a task",
            vendor=_vendor,
            vendor_rep="Jane Doe",
            contact_num="9197779311",
            documentation="",
            cost=0.00,
            notes="This is a test."
        )

        self.assertEqual(str(_task), "Test a task")
