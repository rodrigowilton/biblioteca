# Generated by Django 5.0.6 on 2024-06-02 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0004_alter_livros_data_cadastro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='livros',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='livro.categoria'),
            preserve_default=False,
        ),
    ]
