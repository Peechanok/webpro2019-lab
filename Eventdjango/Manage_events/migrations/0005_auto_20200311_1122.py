# Generated by Django 3.0.2 on 2020-03-11 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manage_events', '0004_auto_20200311_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(upload_to='media'),
        ),
    ]
