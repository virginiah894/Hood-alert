# Generated by Django 2.0 on 2020-01-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_auto_20200119_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to='profile/'),
        ),
    ]
