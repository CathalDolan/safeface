# Generated by Django 3.1.7 on 2021-03-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20210327_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletteruser',
            name='email',
            field=models.EmailField(default=False, max_length=254),
        ),
    ]