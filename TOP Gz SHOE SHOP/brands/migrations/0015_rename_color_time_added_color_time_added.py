# Generated by Django 4.2.3 on 2023-07-10 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0014_color_color_time_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='color_time_added',
            new_name='time_added',
        ),
    ]