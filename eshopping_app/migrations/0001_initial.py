# Generated by Django 4.1.6 on 2023-02-15 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.CharField(max_length=250, unique=True)),
                ('details', models.TextField()),
                ('image', models.ImageField(upload_to='cat_pics')),
            ],
        ),
        migrations.CreateModel(
            name='products_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.CharField(max_length=250, unique=True)),
                ('details', models.TextField()),
                ('image', models.ImageField(upload_to='pro_pics')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('stock', models.IntegerField(default='0')),
                ('available', models.BooleanField(default=False)),
                ('entered', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshopping_app.categories_db')),
            ],
        ),
    ]
