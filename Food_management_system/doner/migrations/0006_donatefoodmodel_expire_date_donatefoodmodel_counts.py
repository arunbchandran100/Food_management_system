# Generated by Django 4.1.7 on 2023-06-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doner', '0005_rename_username_feedbackmodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='donatefoodmodel',
            name='Expire_date',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AddField(
            model_name='donatefoodmodel',
            name='counts',
            field=models.IntegerField(default=10),
        ),
    ]
