# Generated by Django 5.1.6 on 2025-05-31 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dk', '0005_remove_record_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='profit',
        ),
        migrations.AddField(
            model_name='record',
            name='total_profit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
