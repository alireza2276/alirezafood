# Generated by Django 5.0 on 2024-01-04 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_customer_order_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='customer',
        ),
    ]