# Generated by Django 3.2.15 on 2022-09-26 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('sex', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
