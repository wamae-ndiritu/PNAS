# Generated by Django 4.1 on 2023-06-28 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_bodybuildergoal_bodyexpectantmothergoal_diabeticgoal_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BodyExpectantMotherGoal',
            new_name='ExpectantMotherGoal',
        ),
    ]
