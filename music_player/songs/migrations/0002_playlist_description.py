# Generated by Django 5.1.4 on 2025-01-10 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
