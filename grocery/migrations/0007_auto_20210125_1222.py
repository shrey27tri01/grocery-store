# Generated by Django 3.1.5 on 2021-01-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0006_groceryitem_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='date',
            field=models.DateField(),
        ),
    ]
