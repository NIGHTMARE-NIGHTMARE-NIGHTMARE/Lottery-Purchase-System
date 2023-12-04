# Generated by Django 4.2.3 on 2023-12-04 17:53

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('LPSApp', '0018_alter_ticket_next_draw_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousWinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('winning_amount', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(9999999999.99)])),
                ('win_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('ticketType', models.CharField(max_length=200)),
            ],
        ),
    ]