# Generated by Django 2.1.3 on 2018-11-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_auto_20181124_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
