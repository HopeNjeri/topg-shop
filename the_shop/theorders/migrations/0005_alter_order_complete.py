# Generated by Django 4.2 on 2023-06-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theorders', '0004_alter_order_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
