# Generated by Django 3.1.3 on 2020-12-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srapp', '0010_auto_20201113_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdata',
            name='Alt_phone',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='Costumer_Id',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='Price',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='phone',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='sno',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
