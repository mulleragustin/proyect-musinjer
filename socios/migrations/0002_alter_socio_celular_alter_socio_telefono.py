# Generated by Django 5.1 on 2024-09-02 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='celular',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='socio',
            name='telefono',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
