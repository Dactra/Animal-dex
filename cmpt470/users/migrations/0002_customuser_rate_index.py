# Generated by Django 2.2.4 on 2019-08-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='rate_index',
            field=models.IntegerField(default=1),
        ),
    ]