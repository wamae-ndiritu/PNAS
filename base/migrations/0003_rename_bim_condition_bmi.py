# Generated by Django 4.1 on 2023-06-27 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_condition_goal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='condition',
            old_name='bim',
            new_name='bmi',
        ),
    ]
