# Generated by Django 3.0.8 on 2020-07-29 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('order', models.CharField(max_length=5000)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
