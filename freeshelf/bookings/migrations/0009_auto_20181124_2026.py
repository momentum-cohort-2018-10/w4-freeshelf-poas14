# Generated by Django 2.1.3 on 2018-11-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_auto_20181124_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(),
        ),
    ]
