# Generated by Django 4.1.5 on 2023-02-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0005_package_totalseet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Packageid', models.CharField(max_length=225)),
                ('Packagename', models.CharField(max_length=225)),
                ('Username', models.CharField(max_length=225)),
                ('Useremail', models.CharField(max_length=225)),
                ('dateofbook', models.DateField(max_length=225)),
                ('Totalamount', models.CharField(max_length=225)),
                ('Totalperson', models.CharField(max_length=225)),
            ],
        ),
    ]
