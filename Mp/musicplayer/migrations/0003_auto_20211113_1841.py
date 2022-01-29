# Generated by Django 3.2.7 on 2021-11-13 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicplayer', '0002_musicdb_song_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicdb',
            name='id',
        ),
        migrations.AddField(
            model_name='musicdb',
            name='song_id',
            field=models.BigAutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]