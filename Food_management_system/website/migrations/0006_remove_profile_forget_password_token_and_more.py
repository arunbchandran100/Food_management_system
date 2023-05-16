# Generated by Django 4.1.7 on 2023-05-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='forget_password_token',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
