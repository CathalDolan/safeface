# Generated by Django 3.1.7 on 2021-03-20 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_remove_orderlineitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
