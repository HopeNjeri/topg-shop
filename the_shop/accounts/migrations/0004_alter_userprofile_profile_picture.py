# Generated by Django 4.2 on 2023-06-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_userprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, height_field='image_height', null=True, upload_to='user_profiles/', width_field='image_width'),
        ),
    ]
