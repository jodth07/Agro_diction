# Generated by Django 2.1.1 on 2018-12-12 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.RemoveField(
            model_name='stylist',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='stylist',
            name='image',
        ),
        migrations.RemoveField(
            model_name='stylist',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Stylist',
        ),
    ]
