from django.db import models
from .customer import Customer

class Mail(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default='',blank=True, null=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=200, default="")
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name},{self.email}"

    def saveMail(self):
        self.save()

    