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
