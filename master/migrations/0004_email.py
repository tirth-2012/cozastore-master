# Generated by Django 5.1.4 on 2025-03-04 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.CharField(max_length=500)),
            ],
        ),
    ]
