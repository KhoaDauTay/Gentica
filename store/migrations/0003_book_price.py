# Generated by Django 3.0.7 on 2020-06-21 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200621_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=20),
            preserve_default=False,
        ),
    ]