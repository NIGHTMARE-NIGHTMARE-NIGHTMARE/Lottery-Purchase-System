# Generated by Django 4.2.1 on 2023-11-22 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LPSApp', '0004_alter_ticket_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='next_draw_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='ticket',
            name='powerball',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ticket',
            name='previous_draw_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='ticket',
            name='previuous_draw_number_1',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='ticket',
            name='previuous_draw_number_2',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='ticket',
            name='previuous_draw_number_3',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='ticket',
            name='previuous_draw_number_4',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='ticket',
            name='previuous_draw_number_5',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='ticket',
            name='previuous_draw_number_6',
            field=models.IntegerField(default=None),
        ),
    ]
