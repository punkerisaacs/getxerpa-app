import uuid
from django.db import models
from django.db.models import Sum

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    limit = models.DecimalField(max_digits = 15, decimal_places=2)
        
    def totalAmount(self):
        totalAmount = self.transaction_set.aggregate(Sum('amount'))
        print(totalAmount)
        return totalAmount['amount__sum']
 
    def transactionCount(self):
        transactionCount = self.transaction_set.count()
        return transactionCount

    def __float__(self):
        return float(self.limit)

    def spent(self):
        totalAmount = totalAmount = self.transaction_set.filter(ignore = False).aggregate(Sum('amount'))
        if self.limit == 0:
            return 0
        else:
            return float(format((totalAmount['amount__sum'] / self.limit) * 100, ".2f"))

    def available(self):
        totalAmount = self.totalAmount()
        if self.limit == 0:
            return 0
        else:
            return self.limit - totalAmount

    def is_limit_exceeded(self):
        if self.limit == 0:
            return False
        else:
            return self.spent() >= 100

    def __str__(self):
        return "{} - {}".format(self.name, self.id)

    class Meta:
        db_table = 'categories'