# Generated by Django 4.1.4 on 2022-12-20 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_base_email_alter_base_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='base',
            name='email',
            field=models.EmailField(default='', max_length=20),
        ),
    ]
