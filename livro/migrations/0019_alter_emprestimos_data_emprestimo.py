# Generated by Django 5.0.6 on 2024-06-08 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0018_alter_emprestimos_avaliacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 8, 9, 35, 16, 725122)),
        ),
    ]