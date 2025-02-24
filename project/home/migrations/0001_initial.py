# Generated by Django 5.1.4 on 2025-02-19 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=100)),
                ('prodect', models.IntegerField()),
                ('branding', models.CharField(max_length=150)),
                ('books', models.CharField(choices=[('FILE_BOOK', 'LIST_BOOK')], max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('call', models.CharField(max_length=20)),
                ('send', models.TextField()),
            ],
        ),
    ]
