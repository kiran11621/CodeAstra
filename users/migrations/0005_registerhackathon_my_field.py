# Generated by Django 3.0.5 on 2023-02-17 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20230217_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerhackathon',
            name='my_field',
            field=models.CharField(choices=[('a', 'Hola'), ('b', 'Hello'), ('c', 'Bonjour'), ('d', 'Boas')], default='a', max_length=1),
        ),
    ]
