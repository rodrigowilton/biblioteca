# Generated by Django 5.0.4 on 2024-06-03 19:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0009_emprestimo_nome_emprestado_anonimmo_and_more'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='nome_emprestado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
        ),
    ]
