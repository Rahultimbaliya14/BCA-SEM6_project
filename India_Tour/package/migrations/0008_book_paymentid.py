# Generated by Django 4.1.5 on 2023-03-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0007_book_confermationnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='PaymentId',
            field=models.CharField(default=0, max_length=225),
            preserve_default=False,
        ),
    ]
