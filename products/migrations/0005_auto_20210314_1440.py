# Generated by Django 3.1.7 on 2021-03-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210314_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_1',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
        ),
        migrations.AddField(
            model_name='product',
            name='price_2',
            field=models.DecimalField(decimal_places=2, default=0.9, max_digits=6),
        ),
        migrations.AddField(
            model_name='product',
            name='price_3',
            field=models.DecimalField(decimal_places=2, default=0.8, max_digits=6),
        ),
        migrations.AddField(
            model_name='product',
            name='price_4',
            field=models.DecimalField(decimal_places=2, default=0.7, max_digits=6),
        ),
        migrations.AddField(
            model_name='product',
            name='price_5',
            field=models.DecimalField(decimal_places=2, default=0.6, max_digits=6),
        ),
        migrations.AddField(
            model_name='product',
            name='qty_1',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='product',
            name='qty_2',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='product',
            name='qty_3',
            field=models.IntegerField(default=250),
        ),
        migrations.AddField(
            model_name='product',
            name='qty_4',
            field=models.IntegerField(default=500),
        ),
        migrations.AddField(
            model_name='product',
            name='qty_5',
            field=models.IntegerField(default=1000),
        ),
    ]