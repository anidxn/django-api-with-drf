# Generated by Django 5.0 on 2024-05-28 18:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0007_alter_task_uid_alter_timingtask_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('f65edd62-ccd9-46df-b877-ba17e8315d6c'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='timingtask',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('f65edd62-ccd9-46df-b877-ba17e8315d6c'), editable=False, primary_key=True, serialize=False),
        ),
    ]
