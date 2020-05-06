# Generated by Django 3.0.5 on 2020-05-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weapon',
            options={'verbose_name': '武器', 'verbose_name_plural': '武器'},
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='email',
        ),
        migrations.AlterField(
            model_name='weapon',
            name='atk',
            field=models.IntegerField(default=1, verbose_name='攻撃力'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='名前'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='price',
            field=models.IntegerField(default=0, verbose_name='値段'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='required_arm',
            field=models.IntegerField(default=1, verbose_name='必要腕力'),
        ),
    ]
