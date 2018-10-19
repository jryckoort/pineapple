# Generated by Django 2.1.1 on 2018-10-13 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_auto_20181013_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='accountingentry',
            name='text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='compensationaccount',
            name='text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='forecastedaccountingentry',
            name='text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
