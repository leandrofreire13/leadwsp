# Generated by Django 4.0.4 on 2022-05-12 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('referidos', '0010_aluno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='cliente',
        ),
        migrations.AlterField(
            model_name='referido',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='referidos.aluno'),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]