from django.db import models


class Vehicle(models.Model):
    """
    Model defines a vehicle which has make, model, year
    vin, license_plate and color.
    """
    make = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    year = models.CharField(max_length=4)
    vin = models.CharField(max_length=17)
    license_plate = models.CharField(max_length=8)
    color = models.CharField(max_length=15)

    def __str__(self):
        """
            Represent vehicle class object as a string consisting of the
            year, make and model.
            """
        return self.year + ' ' + self.make + ' ' + self.model


class Dealership(models.Model):
    """
    Model defines a dealership which has name, address, city
    state, postal code and office number.
    """
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=4)
    _state = models.CharField(max_length=17)
    postal_code = models.CharField(max_length=8)
    office_number = models.CharField(max_length=15)

    def __str__(self):
        """
            Represent dealership class object as a string consisting of the
            dealership name.
            """
        return self.name
