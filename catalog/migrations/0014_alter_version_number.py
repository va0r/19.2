# Generated by Django 4.2.4 on 2023-08-06 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_remove_version_only_one_active_version_is_possible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='number',
            field=models.SmallIntegerField(verbose_name='Номер версии'),
        ),
    ]
