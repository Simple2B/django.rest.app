# Generated by Django 4.1.1 on 2022-09-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_remove_userprofile_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default=1111, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
