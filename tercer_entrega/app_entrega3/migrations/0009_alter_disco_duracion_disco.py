# Generated by Django 4.2.6 on 2024-01-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_entrega3', '0008_alter_temas_duracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disco',
            name='duracion_disco',
            field=models.IntegerField(),
        ),
    ]
