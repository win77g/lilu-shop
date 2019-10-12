# Generated by Django 2.2.4 on 2019-09-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190830_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_addres',
            new_name='customer_city',
        ),
        migrations.AddField(
            model_name='order',
            name='customer_street',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
