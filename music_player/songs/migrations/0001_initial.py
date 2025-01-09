# Generated by Django 5.1.4 on 2025-01-09 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(blank=True, max_length=100, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('file', models.FileField(upload_to='songs/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers/')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('songs', models.ManyToManyField(related_name='playlists', to='songs.song')),
            ],
        ),
    ]
