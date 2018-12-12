# Generated by Django 2.1.1 on 2018-12-12 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181212_0107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='category',
        ),
        migrations.AddField(
            model_name='user',
            name='clearance',
            field=models.CharField(choices=[('Definer', 'Definer'), ('Reviewer', 'Reviewer'), ('Publisher', 'Publisher')], default='Definer', max_length=8),
        ),
    ]
