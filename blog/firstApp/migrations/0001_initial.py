# Generated by Django 2.2.5 on 2019-12-13 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('level', models.IntegerField()),
                ('summary', models.TextField(max_length=20)),
            ],
        ),
    ]