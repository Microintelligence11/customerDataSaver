# Generated by Django 3.1.1 on 2020-11-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srapp', '0004_auto_20201111_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdata',
            name='Date',
            field=models.DateField(blank=True),
        ),
    ]
