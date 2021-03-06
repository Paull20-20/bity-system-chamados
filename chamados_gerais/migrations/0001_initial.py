# Generated by Django 4.0.1 on 2022-03-18 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamado_geral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título:')),
                ('descrição', models.TextField(verbose_name='Descrição:')),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='', verbose_name='Anexo:')),
                ('Status', models.CharField(choices=[('Solicitado', 'Solicitado'), ('Em_andamento', 'Em_andamento'), ('Concluído', 'Concluído')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
