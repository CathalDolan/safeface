# Generated by Django 3.1.7 on 2021-03-28 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_userprofile_default_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_full_name',
            new_name='full_name',
        ),
    ]
