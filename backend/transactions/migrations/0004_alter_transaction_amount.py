# Generated by Django 4.2.4 on 2023-08-19 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]