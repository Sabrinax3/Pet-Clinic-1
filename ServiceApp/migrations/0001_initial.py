# Generated by Django 3.0.5 on 2020-05-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='SOME STRING', max_length=20)),
                ('Description', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
