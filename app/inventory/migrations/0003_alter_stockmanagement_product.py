# Generated by Django 5.2 on 2025-04-08 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_stockmanagement_last_checked_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmanagement',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='inventory.product'),
        ),
    ]
