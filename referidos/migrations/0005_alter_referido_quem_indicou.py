# Generated by Django 3.2.8 on 2021-10-29 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referidos', '0004_referido_quem_indicou'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referido',
            name='quem_indicou',
            field=models.CharField(default='', max_length=200),
        ),
    ]