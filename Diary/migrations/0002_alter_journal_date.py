# Generated by Django 3.2.15 on 2022-10-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
