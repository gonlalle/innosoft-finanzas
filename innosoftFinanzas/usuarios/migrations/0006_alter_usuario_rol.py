# Generated by Django 3.2.8 on 2021-12-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_usuario_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('NA', 'NADA'), ('MB', 'MIEMBRO'), ('CD', 'COORDINADOR'), ('PR', 'PROFESOR'), ('SU', 'SUPERUSER')], default='NA', max_length=2),
        ),
    ]
