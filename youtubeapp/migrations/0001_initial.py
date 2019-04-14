# Generated by Django 2.1.7 on 2019-03-04 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(default=None, max_length=200)),
                ('channel_name', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ChannelStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_views', models.IntegerField(default=None)),
                ('time_stamp', models.DateTimeField(auto_now=True)),
                ('channel_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtubeapp.ChannelMaster')),
            ],
        ),
        migrations.CreateModel(
            name='VideoMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(default=None, max_length=200)),
                ('video_name', models.CharField(default=None, max_length=200)),
                ('channel_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtubeapp.ChannelMaster')),
            ],
        ),
        migrations.CreateModel(
            name='VideoStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_views', models.IntegerField(default=None)),
                ('time_stamp', models.DateTimeField(auto_now=True)),
                ('video_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtubeapp.VideoMaster')),
            ],
        ),
    ]
