# Generated by Django 5.1.4 on 2025-02-19 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='are',
            old_name='password',
            new_name='passwordss',
        ),
        migrations.RenameField(
            model_name='are',
            old_name='s_id',
            new_name='t_id',
        ),
        migrations.RenameField(
            model_name='are',
            old_name='s_lname',
            new_name='t_lname',
        ),
        migrations.RenameField(
            model_name='are',
            old_name='s_name',
            new_name='t_name',
        ),
        migrations.RenameField(
            model_name='use',
            old_name='ts_id',
            new_name='s_id',
        ),
    ]
