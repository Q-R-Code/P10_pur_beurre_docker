# Generated by Django 3.1.7 on 2021-03-31 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_auto_20210331_1614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Product'},
        ),
    ]
