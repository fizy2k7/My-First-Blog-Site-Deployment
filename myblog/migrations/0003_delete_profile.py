# Generated by Django 2.2.4 on 2019-09-13 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]