# Generated by Django 3.0.5 on 2020-05-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0002_auto_20200504_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='name',
            field=models.CharField(max_length=100, verbose_name='名前'),
        ),
    ]