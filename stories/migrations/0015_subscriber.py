# Generated by Django 2.2.8 on 2020-01-07 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0014_story_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
