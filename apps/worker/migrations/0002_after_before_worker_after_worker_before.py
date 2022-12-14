# Generated by Django 4.1.3 on 2022-12-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='After',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Before',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='worker',
            name='after',
            field=models.ManyToManyField(to='worker.after'),
        ),
        migrations.AddField(
            model_name='worker',
            name='before',
            field=models.ManyToManyField(to='worker.before'),
        ),
    ]
