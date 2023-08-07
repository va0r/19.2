# Generated by Django 4.2.4 on 2023-08-06 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_alter_version_number'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='version',
            constraint=models.UniqueConstraint(condition=models.Q(('is_active', True)), fields=('is_active',), name='Only one active version is possible'),
        ),
    ]