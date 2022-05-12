# Generated by Django 4.0.4 on 2022-05-12 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referidos', '0007_aluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('prioridade', models.BooleanField()),
                ('status', models.CharField(choices=[('Iniciar', 'INICIAR'), ('Ligação 1', 'LIGACAO_1'), ('Ligação 2', 'LIGACAO_2'), ('Ligação 3', 'LIGACAO_3'), ('Mandar áudio', 'MANDA_AUDIO'), ('Áudio enviado', 'AUDIO_ENVIADO'), ('Agendado', 'AGENDADO'), ('Mandar texto', 'MANDAR_TEXTO'), ('Texto enviado', 'TEXTO_ENVIADO'), ('Não venda', 'NAO_VENDA'), ('Venda', 'VENDA')], default='Iniciar', max_length=200)),
            ],
        ),
    ]