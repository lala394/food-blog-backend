# Generated by Django 2.2.7 on 2019-12-04 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_story'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ('created_at',), 'verbose_name': 'Story', 'verbose_name_plural': 'Stories'},
        ),
    ]
