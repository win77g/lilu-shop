# Generated by Django 2.2.4 on 2019-09-23 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0012_auto_20190924_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filtercategory',
            name='name',
            field=models.CharField(blank=True, default='', max_length=250, unique=True),
        ),
    ]
