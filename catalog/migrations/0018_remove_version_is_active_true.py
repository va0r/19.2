# Generated by Django 4.2.4 on 2023-08-07 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_remove_version_is_active_true_version_is_active_true'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='version',
            name='is_active_True',
        ),
    ]
