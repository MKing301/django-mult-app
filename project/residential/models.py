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
    email = models.EmailField(max_length=255, blank=True)
    website = models.TextField(blank=True)

    def __str__(self):
        """
        Represent vendor class object as a string consisting of the
        vendor's name.
        """
        return self.name


class Task(models.Model):
    """
    Model defines a task performed by a vendor which has
    task_date, name, vendor, vendor_rep, contact_num, documentation,
    cost and notes.
    """
    task_date = models.DateField()
    name = models.CharField(max_length=60)
    vendor = models.ForeignKey(
        Vendor,
        blank=True,
        on_delete=models.CASCADE
    )
    vendor_rep = models.CharField(max_length=50, blank=True)
    contact_num = models.CharField(max_length=10, blank=True)
    documentation = models.TextField(blank=True)
    cost = models.DecimalField(blank=True, max_digits=8, decimal_places=2)
    notes = models.TextField(blank=True)

    def __str__(self):
        """
        Represent task class object as a string consisting of the
        task's name.
        """
        return self.name
