# Generated by Django 3.2 on 2021-05-19 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0013_search_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='search_history',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
