# Generated by Django 4.2.4 on 2023-09-11 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='like',
            new_name='show',
        ),
        migrations.DeleteModel(
            name='commentreplay',
        ),
    ]
