# Generated by Django 2.0.2 on 2018-02-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180217_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='jv',
            field=models.BooleanField(default=0),
        ),
    ]
