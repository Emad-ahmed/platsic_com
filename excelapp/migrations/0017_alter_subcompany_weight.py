# Generated by Django 4.2 on 2023-05-17 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excelapp', '0016_clientcompany_urlname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcompany',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
