# Generated by Django 3.2.4 on 2021-07-28 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chioce',
            new_name='Choice',
        ),
    ]
