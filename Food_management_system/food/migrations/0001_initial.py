# Generated by Django 4.1.7 on 2023-05-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonateFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_type', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('supply_date', models.DateField()),
                ('pickup_location', models.CharField(max_length=100)),
                ('pickup_deadline', models.DateField()),
                ('contact_information', models.CharField(max_length=100)),
            ],
        ),
    ]
