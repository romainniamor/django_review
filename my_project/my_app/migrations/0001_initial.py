# Generated by Django 5.0.6 on 2024-05-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('laste_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
