# Generated by Django 4.2 on 2023-06-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theorders', '0003_shippingaddress_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3),
        ),
    ]
