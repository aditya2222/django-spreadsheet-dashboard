# Generated by Django 2.0.7 on 2018-07-19 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20180719_0600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spreadsheetmodel',
            old_name='percentage_of_available',
            new_name='percentage_of_available_funds',
        ),
    ]
