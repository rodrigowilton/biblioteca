# Generated by Django 5.0.6 on 2024-06-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0002_alter_livros_options_alter_livros_co_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True),
        ),
    ]