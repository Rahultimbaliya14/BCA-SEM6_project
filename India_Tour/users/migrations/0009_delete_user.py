# Generated by Django 4.1.3 on 2022-12-17 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_mail_alter_user_phonenumber'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
