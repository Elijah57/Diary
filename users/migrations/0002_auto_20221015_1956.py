# Generated by Django 3.2.15 on 2022-10-15 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]