# Generated by Django 4.2 on 2023-04-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excelapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcompany',
            name='Invoicenumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subcompany',
            name='invoicedate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subcompany',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
