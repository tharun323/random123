# Generated by Django 2.0 on 2019-03-05 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelstats',
            name='total_views',
            field=models.BigIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='videostats',
            name='total_views',
            field=models.BigIntegerField(default=None),
        ),
    ]
