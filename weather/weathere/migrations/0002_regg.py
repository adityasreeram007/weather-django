# Generated by Django 2.0.2 on 2019-10-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weathere', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='regg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('passer', models.CharField(max_length=20)),
                ('confpasser', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
