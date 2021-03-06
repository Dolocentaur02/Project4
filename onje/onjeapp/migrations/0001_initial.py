# Generated by Django 2.2.5 on 2019-09-10 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Full name')),
                ('address1', models.CharField(max_length=500, verbose_name='Address line1')),
                ('address2', models.CharField(max_length=500, verbose_name='Address line2')),
                ('zip_code', models.CharField(max_length=10, verbose_name='ZIP/ Postal Code')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
            ],
        ),
    ]
