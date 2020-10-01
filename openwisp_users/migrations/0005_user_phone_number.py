# Generated by Django 2.1.7 on 2019-04-03 14:52

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [('openwisp_users', '0004_default_groups')]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, unique=True, max_length=128, null=True, region=None
            ),
        )
    ]
