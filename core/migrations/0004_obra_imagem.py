# Generated by Django 5.1.6 on 2025-03-04 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/'),
        ),
    ]
