# Generated by Django 2.1.1 on 2018-11-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_auto_20181108_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='nickname',
            field=models.CharField(default='DEFAULT', max_length=128),
        ),
    ]
