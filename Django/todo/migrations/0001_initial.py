# Generated by Django 3.1.7 on 2021-03-12 14:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(help_text='Enter a task', max_length=200, validators=[django.core.validators.MinLengthValidator(1, 'Task must be greater than 1 character')])),
                ('description', models.CharField(help_text='Enter the description of your task', max_length=500)),
            ],
        ),
    ]
