# Generated by Django 4.1.4 on 2022-12-20 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='base',
            name='email',
            field=models.EmailField(default='', max_length=20),
        ),
    ]
