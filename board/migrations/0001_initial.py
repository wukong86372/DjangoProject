# Generated by Django 2.1 on 2018-08-04 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('text', models.CharField(max_length=1024)),
                ('data_added', models.DateTimeField(auto_now_add=True)),
                ('likeNum', models.IntegerField()),
                ('dislikeNum', models.IntegerField()),
            ],
        ),
    ]
