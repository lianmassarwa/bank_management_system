# Generated by Django 5.1.2 on 2024-10-19 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(default='default_password', max_length=128),
        ),
    ]
