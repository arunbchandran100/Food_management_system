# Generated by Django 4.2 on 2023-05-19 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doner', '0004_feedbackmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbackmodel',
            old_name='username',
            new_name='user',
        ),
    ]