# Generated by Django 4.2.5 on 2023-10-17 22:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_expense_description_income_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('type_x', models.CharField(default='', max_length=10)),
                ('description', models.TextField(blank=True, max_length=100)),
                ('entry', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.wallet')),
            ],
        ),
    ]
