# Generated by Django 5.0.1 on 2024-01-10 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0002_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('test_col', models.IntegerField()),
            ],
        ),
    ]