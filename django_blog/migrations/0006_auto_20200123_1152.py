# Generated by Django 3.0.2 on 2020-01-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_blog', '0005_auto_20200122_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='post_pics'),
        ),
    ]
