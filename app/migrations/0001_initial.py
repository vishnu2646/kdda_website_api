# Generated by Django 3.2 on 2025-05-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=255)),
                ('background_color', models.CharField(blank=True, max_length=7, null=True)),
                ('cover_image', models.URLField(blank=True, null=True)),
                ('images', models.JSONField(blank=True, default=list)),
            ],
        ),
    ]
