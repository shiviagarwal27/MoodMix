# Generated by Django 3.2.7 on 2021-11-14 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicplayer', '0009_auto_20211114_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicdb',
            name='image',
            field=models.ImageField(default='image', upload_to='image'),
        ),
    ]