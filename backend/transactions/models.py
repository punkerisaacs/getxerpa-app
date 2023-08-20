import uuid
from django.db import models
from categories.models import *

def generate_id():
    return str(uuid.uuid4()).split("-")[-1]

# Create your models here.
class Transaction(models.Model):
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits = 15, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    ignore = models.BooleanField(default=False)

    def hour(self):
        return self.date.strftime("%I:%M%p")

    def __str__(self):
        return "{} - {}".format(self.description, self.id)

    class Meta:
        db_table = 'transactions'