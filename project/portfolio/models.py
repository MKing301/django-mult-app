from django.db import models


class Contact(models.Model):
    """
    Model defines a contact which has first name, last name, email address and request.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    user_request =  models.TextField()

    def __str__(self):
        """
        Represent Contact class object as a string consisting of the first name, space and last name.
        """
        return self.first_name + ' ' + self.last_name