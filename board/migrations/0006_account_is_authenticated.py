# Generated by Django 2.1 on 2018-08-05 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20180805_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_authenticated',
            field=models.BooleanField(default=False, verbose_name=False),
        ),
    ]
