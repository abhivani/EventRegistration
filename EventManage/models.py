from django.db import models


class eventregister(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.IntegerField()
    passoutyear = models.IntegerField()
    course = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()

    def register(self):
        self.save()