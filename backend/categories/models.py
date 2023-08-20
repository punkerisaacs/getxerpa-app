import uuid
import datetime
from django.db import models
from django.db.models import Sum

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    limit = models.DecimalField(max_digits = 15, decimal_places=2)
    
    def totalAmount(self):
        month = datetime.date.today().month
        totalAmount = self.transaction_set.filter(date__month = month).aggregate(Sum('amount'))
        return totalAmount['amount__sum'] or 0
 
    def spent(self):
        month = datetime.date.today().month
        totalAmount = self.transaction_set.filter(ignore = False, date__month = month).aggregate(Sum('amount'))
        if self.limit == 0:
            return 0
        else:
            return round(((totalAmount['amount__sum'] or 0) / self.limit) * 100)

    def transactionCount(self):
        month = datetime.date.today().month
        return self.transaction_set.filter(date__month = month).count()

    def available(self):
        totalAmount = self.totalAmount()
        if self.limit == 0:
            return 0
        else:
            return self.limit - totalAmount
    
    def is_limit_exceeded(self):
        if self.limit == 0:
            return 0
        else:
            return int(self.spent() >= 100)

    def __str__(self):
        return "{} - {}".format(self.name, self.id)

    class Meta:
        db_table = 'categories'