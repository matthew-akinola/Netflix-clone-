# Generated by Django 3.2.5 on 2021-08-11 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='uname',
            new_name='users',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='uname',
            new_name='users',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='uname',
            new_name='users',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='uname',
            new_name='users',
        ),
    ]
