# Generated by Django 2.1.1 on 2018-12-11 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0002_auto_20181207_0604'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('category', models.CharField(choices=[('Costumer', 'Costumer'), ('Stylist', 'Stylist')], default='Costumer', max_length=8)),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateField(auto_now=True)),
                ('phone', models.CharField(blank=True, default='', max_length=18)),
                ('is_stylist', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='images.Image')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_type', models.CharField(choices=[('Billing', 'Billing'), ('Shipping', 'Shipping'), ('Shop', 'Shop')], default='Shipping', max_length=10)),
                ('street', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('zipcode', models.CharField(max_length=10)),
                ('Country', models.CharField(blank=True, default='United States', max_length=15)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stylist',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Costumer', 'Costumer'), ('Stylist', 'Stylist')], default='Costumer', max_length=8)),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('title', models.CharField(blank=True, max_length=120)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('description', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(blank=True, default='', max_length=18)),
                ('is_stylist', models.BooleanField(default=True)),
                ('gallery', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='images.Gallery')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='images.Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
