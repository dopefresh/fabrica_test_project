# Generated by Django 2.2.10 on 2021-08-03 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20210803_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='polls.Quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='quizzes', to='polls.User'),
        ),
    ]
