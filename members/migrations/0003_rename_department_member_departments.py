# Generated by Django 4.2.4 on 2023-11-18 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_member_team_delete_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='department',
            new_name='departments',
        ),
    ]
