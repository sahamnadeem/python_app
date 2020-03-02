# Generated by Django 3.0.2 on 2020-03-01 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='about',
            field=models.CharField(default=None, max_length=80),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='avatar',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='cover_photo',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='skills',
            field=models.CharField(default=None, max_length=80),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='web_url',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='country',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]