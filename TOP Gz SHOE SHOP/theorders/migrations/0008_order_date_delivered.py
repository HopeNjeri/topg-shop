# Generated by Django 4.2 on 2023-07-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theorders', '0007_alter_order_date_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_delivered',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]