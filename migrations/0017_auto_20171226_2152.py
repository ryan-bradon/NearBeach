# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 10:52
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0016_quotes_products_and_services_sales_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes_products_and_services',
            name='discount_percent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
