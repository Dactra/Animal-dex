# Generated by Django 2.2.3 on 2019-07-18 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_remove_animal_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='image_url',
            field=models.CharField(max_length=400),
        ),
    ]
