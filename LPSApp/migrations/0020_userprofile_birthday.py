# Generated by Django 4.2.3 on 2023-12-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LPSApp', '0019_previouswinner'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]