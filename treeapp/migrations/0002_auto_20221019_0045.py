# Generated by Django 2.2.4 on 2022-10-18 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='planted_by',
            field=models.CharField(max_length=255, null=True),
        ),
    ]