# Generated by Django 5.2.1 on 2025-05-31 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='role',
            field=models.CharField(choices=[('Agent', 'agent'), ('Testimonial', 'testimonial')], default='Agent', max_length=50),
        ),
    ]
