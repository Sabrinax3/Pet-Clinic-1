# Generated by Django 3.0.5 on 2020-04-21 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_auto_20200415_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfotable',
            name='image',
            field=models.ImageField(default='users_image/default.jpg', upload_to='users_image'),
        ),
    ]
