# Generated by Django 2.1.1 on 2021-08-06 19:05

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20210806_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(default='avatar/1.png', upload_to='avatar/%Y%m%d/'),
        ),
    ]
