# Generated by Django 4.1.3 on 2022-12-12 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_after_before_worker_after_worker_before'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='after',
            options={'ordering': ['-title']},
        ),
        migrations.AlterModelOptions(
            name='before',
            options={'ordering': ['-title']},
        ),
    ]
