# Generated by Django 4.2.4 on 2023-08-06 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_remove_version_unique_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='version',
            name='Only one active version is possible',
        ),
    ]
