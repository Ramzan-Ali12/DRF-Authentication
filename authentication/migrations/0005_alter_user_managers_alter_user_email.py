# Generated by Django 5.0.1 on 2024-01-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_groups_alter_user_user_permissions'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
