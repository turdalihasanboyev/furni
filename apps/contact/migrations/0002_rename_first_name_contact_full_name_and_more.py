# Generated by Django 5.2.1 on 2025-06-01 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
    ]
