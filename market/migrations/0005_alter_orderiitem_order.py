# Generated by Django 4.2.4 on 2023-08-27 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_rename_comolete_order_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderiitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderitem', to='market.order'),
        ),
    ]