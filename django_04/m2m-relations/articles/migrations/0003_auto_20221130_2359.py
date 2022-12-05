# Generated by Django 3.1.2 on 2022-11-30 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20221130_2007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(through='articles.Scope', to='articles.Tag'),
        ),
    ]
