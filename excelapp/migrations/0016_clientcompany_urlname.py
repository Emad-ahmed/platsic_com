# Generated by Django 4.2 on 2023-05-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excelapp', '0015_subcompany_urlname'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientcompany',
            name='urlname',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]