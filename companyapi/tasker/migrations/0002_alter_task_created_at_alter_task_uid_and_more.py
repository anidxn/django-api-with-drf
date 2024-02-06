# Generated by Django 5.0.1 on 2024-02-06 11:14

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('53470e21-5ea5-4e3b-9c2a-7c0675c3c994'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='updtaed_at',
            field=models.DateField(auto_now=True),
        ),
    ]
