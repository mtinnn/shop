# Generated by Django 4.2.4 on 2023-08-30 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0012_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.customer'),
        ),
    ]
