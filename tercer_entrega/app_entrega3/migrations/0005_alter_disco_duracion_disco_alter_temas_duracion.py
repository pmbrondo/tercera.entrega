# Generated by Django 4.2.6 on 2023-12-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_entrega3', '0004_alter_disco_duracion_disco_alter_temas_duracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disco',
            name='duracion_disco',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='temas',
            name='duracion',
            field=models.DurationField(),
        ),
    ]