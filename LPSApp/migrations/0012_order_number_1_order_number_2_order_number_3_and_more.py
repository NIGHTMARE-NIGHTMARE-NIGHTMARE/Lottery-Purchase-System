# Generated by Django 4.2.3 on 2023-12-03 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LPSApp', '0011_order_ticket_order_ticketcost'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='number_1',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='number_2',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='number_3',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='number_4',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='number_5',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='number_6',
            field=models.IntegerField(default=None, null=True),
        ),
    ]