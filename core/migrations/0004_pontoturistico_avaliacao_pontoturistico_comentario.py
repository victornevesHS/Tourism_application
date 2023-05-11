# Generated by Django 4.2.1 on 2023-05-11 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('comentarios', '0001_initial'),
        ('core', '0003_pontoturistico_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacao',
            field=models.ManyToManyField(to='avaliacoes.avaliacao'),
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='comentario',
            field=models.ManyToManyField(to='comentarios.comentario'),
        ),
    ]