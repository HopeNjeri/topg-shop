# Generated by Django 4.2 on 2023-05-24 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0009_alter_brand_brand_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='brand_image',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='image_width',
        ),
    ]
