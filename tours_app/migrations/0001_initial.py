# Generated by Django 4.1.6 on 2023-02-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='banner_back',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Banner Background', max_length=250)),
                ('image', models.ImageField(upload_to='banner_background')),
            ],
        ),
        migrations.CreateModel(
            name='footer_back',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Footer Background', max_length=250)),
                ('image', models.ImageField(upload_to='footer_background')),
            ],
        ),
        migrations.CreateModel(
            name='header_back',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Header Background', max_length=250)),
                ('image', models.ImageField(upload_to='header_background')),
            ],
        ),
        migrations.CreateModel(
            name='our_team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('image', models.ImageField(upload_to='Our_team_images')),
                ('detail', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='our_tours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('image', models.ImageField(upload_to='Our_tours_images')),
                ('detail', models.TextField(blank=True)),
            ],
        ),
    ]