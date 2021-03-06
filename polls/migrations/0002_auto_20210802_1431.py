# Generated by Django 2.2.10 on 2021-08-02 10:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice_type',
        ),
        migrations.RemoveField(
            model_name='question',
            name='description',
        ),
        migrations.RemoveField(
            model_name='question',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='start_date',
        ),
        migrations.AddField(
            model_name='choice',
            name='answer',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_type',
            field=models.CharField(choices=[('Text', 'Ответ текстом'), ('Choice', 'Выбор варианта'), ('Choices', 'Выбор нескольких вариантов')], default='Text', max_length=20),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='choice',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.User'),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.Quiz'),
        ),
    ]
