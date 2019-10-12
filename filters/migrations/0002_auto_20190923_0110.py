# Generated by Django 2.2.4 on 2019-09-22 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filtercategory',
            name='category',
            field=models.ForeignKey(db_column='filter_category_name', on_delete=django.db.models.deletion.CASCADE, related_name='filtercategories', to='products.Category', verbose_name='Category'),
        ),
    ]
