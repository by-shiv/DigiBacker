# Generated by Django 4.2.2 on 2023-06-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
