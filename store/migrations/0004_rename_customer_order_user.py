# Generated by Django 5.0 on 2024-01-04 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_customer_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='user',
        ),
    ]
