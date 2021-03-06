# Generated by Django 3.0.8 on 2020-11-06 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30, null=True)),
                ('user_read', models.BooleanField()),
                ('admin_read', models.BooleanField()),
                ('last_message', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('sender', models.CharField(max_length=30)),
                ('body', models.CharField(max_length=1000)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatApp.Room')),
            ],
        ),
    ]
