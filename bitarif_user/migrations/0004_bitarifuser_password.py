# Generated by Django 3.0.8 on 2020-09-03 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitarif_user', '0003_auto_20200803_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitarifuser',
            name='password',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]