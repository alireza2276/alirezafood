# Generated by Django 5.0 on 2024-01-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveBigIntegerField(blank=True, default=0),
        ),
    ]
