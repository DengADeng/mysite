# Generated by Django 2.1.7 on 2019-11-08 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
        migrations.AddField(
            model_name='entry',
            name='entry_text',
            field=models.TextField(default=''),
        ),
    ]