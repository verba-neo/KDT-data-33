# Generated by Django 5.0.1 on 2024-01-18 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Counter',
        ),
    ]