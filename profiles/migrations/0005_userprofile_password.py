# Generated by Django 4.1.1 on 2022-09-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_userprofile_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default=12345678, max_length=255),
            preserve_default=False,
        ),
    ]
