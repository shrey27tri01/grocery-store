# Generated by Django 3.1.5 on 2021-01-25 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0003_auto_20210125_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='status',
            field=models.CharField(choices=[('B', 'Bought'), ('P', 'Pending'), ('NA', 'Not Available')], max_length=5),
        ),
    ]
