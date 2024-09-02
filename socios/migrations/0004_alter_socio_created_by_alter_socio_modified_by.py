# Generated by Django 5.1 on 2024-09-02 23:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0003_alter_socio_telefono_laboral'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='socio_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='socio',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='socio_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
