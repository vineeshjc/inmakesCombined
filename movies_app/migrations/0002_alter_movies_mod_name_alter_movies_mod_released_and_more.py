# Generated by Django 4.1.6 on 2023-02-17 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies_mod',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='movies_mod',
            name='released',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='movies_mod',
            name='story',
            field=models.TextField(),
        ),
    ]