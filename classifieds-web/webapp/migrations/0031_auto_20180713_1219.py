# Generated by Django 2.0.7 on 2018-07-13 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0030_offer_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='product_name',
            new_name='product_title',
        ),
    ]
