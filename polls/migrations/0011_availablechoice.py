# Generated by Django 2.2.10 on 2021-08-03 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20210802_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
