# Generated by Django 4.2.3 on 2023-07-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0017_alter_product_shoe_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shoe_size',
            field=models.ManyToManyField(blank=True, to='brands.size'),
        ),
    ]
