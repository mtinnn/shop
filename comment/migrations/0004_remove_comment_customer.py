# Generated by Django 4.2.4 on 2023-09-19 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_remove_comment_show_comment_email_comment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='customer',
        ),
    ]
