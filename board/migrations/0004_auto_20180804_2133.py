# Generated by Django 2.1 on 2018-08-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20180804_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='message',
            name='username',
            field=models.CharField(max_length=512),
        ),
    ]
