# Generated by Django 4.2 on 2023-07-05 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theorders', '0005_alter_order_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]
