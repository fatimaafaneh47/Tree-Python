# Generated by Django 2.2.4 on 2022-10-19 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treeapp', '0003_auto_20221019_1320'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tree',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]