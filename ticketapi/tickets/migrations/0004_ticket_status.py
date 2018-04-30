# Generated by Django 2.0.4 on 2018-04-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20180430_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('CLOSED', 'Closed')], default='pending', max_length=155),
        ),
    ]
