# Generated by Django 3.1.1 on 2020-11-11 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdata',
            name='Date',
            field=models.DateField(),
        ),
    ]
