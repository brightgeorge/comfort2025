# Generated by Django 5.0.1 on 2025-01-30 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch21app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='share_holders',
            name='share_holders_amt_total',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='share_holders',
            name='share_holders_rent',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
