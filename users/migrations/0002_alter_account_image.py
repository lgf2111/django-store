# Generated by Django 4.1 on 2022-09-06 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(default='profile_pics/default.png', upload_to='profile_pics'),
        ),
    ]