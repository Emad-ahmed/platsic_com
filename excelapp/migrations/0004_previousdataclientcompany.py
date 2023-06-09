# Generated by Django 4.2 on 2023-05-20 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excelapp', '0003_rename_nyid_previousdatasubcompany_myid'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousDataClientCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myid', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=100)),
                ('line1', models.CharField(max_length=150)),
                ('line2', models.CharField(max_length=150)),
                ('line3', models.CharField(max_length=150)),
                ('line4', models.CharField(max_length=150)),
                ('urlname', models.CharField(blank=True, max_length=150, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('Invoicenumber', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('invoicedate', models.DateField(blank=True, null=True)),
                ('rangemin', models.FloatField(blank=True, null=True)),
                ('rangemax', models.FloatField(blank=True, null=True)),
                ('head_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='excelapp.headcompany')),
            ],
        ),
    ]
