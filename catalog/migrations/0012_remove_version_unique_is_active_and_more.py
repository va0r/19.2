# Generated by Django 4.2.4 on 2023-08-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_remove_version_is_current_version_description_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='version',
            name='unique_is_active',
        ),
        migrations.AlterField(
            model_name='version',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(verbose_name='Признак активной версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='number',
            field=models.SmallIntegerField(unique=True, verbose_name='Номер версии'),
        ),
        migrations.AddConstraint(
            model_name='version',
            constraint=models.UniqueConstraint(condition=models.Q(('is_active', True)), fields=('is_active',), name='Only one active version is possible'),
        ),
    ]
