# Generated by Django 4.2.4 on 2023-08-18 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('d', models.CharField(blank=True, max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=300)),
                ('amount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('ignore', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
    ]
