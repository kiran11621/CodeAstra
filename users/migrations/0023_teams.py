# Generated by Django 3.0.5 on 2023-02-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_participatehackathon_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('teamname', models.CharField(default=0, max_length=20)),
                ('hackid', models.CharField(default=0, max_length=20)),
            ],
        ),
    ]