from django.db import models


class Vendor(models.Model):
    """
    Model defines a vendor which has name, address, city
    state, postal code and office number.
    """
    name = models.TextField()
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    vendor_state = models.CharField(max_length=2, blank=True)
    postal_code = models.CharField(max_length=8, blank=True)
    office_number = models.CharField(max_length=15, blank=True)
    website = models.TextField(blank=True)

    def __str__(self):
        """
        Represent vendor class object as a string consisting of the
        vendor's name.
        """
        return self.name
