# Generated by Django 4.2.5 on 2023-09-11 07:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_wallet_total_expense_wallet_total_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='last_entry',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
