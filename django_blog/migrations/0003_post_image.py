# Generated by Django 3.0.2 on 2020-01-22 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to='post_pics'),
        ),
    ]
