# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cowork', '0004_auto_20150831_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_logo',
            field=models.ImageField(upload_to='logos', null=True, verbose_name='Company logo'),
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='Company description'),
        ),
        migrations.AddField(
            model_name='company',
            name='phone_number',
            field=models.IntegerField(null=True, verbose_name='Phone number'),
        ),
        migrations.AddField(
            model_name='company',
            name='vat_id',
            field=models.CharField(default='unknown', max_length=32, verbose_name='VAT ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.URLField(null=True, verbose_name='Website'),
        ),
        migrations.AddField(
            model_name='location',
            name='address_line_1',
            field=models.CharField(default='unknown', max_length=200, verbose_name='Address line 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='address_line_2',
            field=models.CharField(default='', max_length=200, verbose_name='Address line 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='address_line_3',
            field=models.CharField(default='', max_length=200, verbose_name='Address line 3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.CharField(default='unknown', max_length=30, verbose_name='Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='postal_code',
            field=models.CharField(default='unknown', max_length=12, verbose_name='Postal code:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=200, verbose_name='City'),
        ),
    ]
