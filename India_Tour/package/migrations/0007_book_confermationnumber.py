# Generated by Django 4.1.5 on 2023-02-05 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0006_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ConfermationNumber',
            field=models.CharField(default=0, max_length=225),
            preserve_default=False,
        ),
    ]
