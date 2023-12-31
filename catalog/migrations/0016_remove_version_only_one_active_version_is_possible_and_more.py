# Generated by Django 4.2.4 on 2023-08-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_version_only_one_active_version_is_possible'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='version',
            name='Only one active version is possible',
        ),
        migrations.AddConstraint(
            model_name='version',
            constraint=models.UniqueConstraint(condition=models.Q(('is_active', True)), fields=('is_active',), name='is_active_True', violation_error_message='Активной может быть только одна версия!'),
        ),
    ]
