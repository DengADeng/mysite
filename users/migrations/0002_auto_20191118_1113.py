# Generated by Django 2.1.7 on 2019-11-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]