# Generated by Django 2.1.3 on 2018-11-24 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0011_auto_20181124_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]
