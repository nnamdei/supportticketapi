# Generated by Django 2.0.4 on 2018-04-30 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20180430_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='user_id',
            new_name='user',
        ),
    ]
